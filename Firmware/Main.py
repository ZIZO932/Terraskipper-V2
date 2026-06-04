import time
import struct
import math
from machine import Pin, PWM, ADC, I2C

LOOP_HZ          = 10
LOOP_PERIOD_MS   = 1000 // LOOP_HZ
SOUND_CM_PER_US  = 0.01716
HCSR04_TIMEOUT   = 30_000
MOTOR_PWM_FREQ   = 20_000
MOTOR_DUTY_FULL  = 65535
SERVO_FREQ       = 50
SERVO_PERIOD_US  = 20_000
MPU_ADDR         = 0x68
MPU_PWR_MGMT_1   = 0x6B
MPU_SMPLRT_DIV   = 0x19
MPU_CONFIG_REG   = 0x1A
MPU_GYRO_CONFIG  = 0x1B
MPU_ACCEL_CONFIG = 0x1C
MPU_ACCEL_XOUT_H = 0x3B
MPU_WHO_AM_I     = 0x75
ACCEL_SCALE      = 16384.0
GYRO_SCALE       = 131.0
OW_SKIP_ROM      = 0xCC
OW_CONVERT_T     = 0x44
OW_READ_SCRATCH  = 0xBE
VREF             = 3.3
ADC_MAX          = 65535
TEMP_COMP_COEFF  = 0.02
MOISTURE_DRY_RAW = 52000
MOISTURE_WET_RAW = 18000

ena = PWM(Pin(16)); ena.freq(MOTOR_PWM_FREQ); ena.duty_u16(0)
in1 = Pin(17, Pin.OUT, value=0)
in2 = Pin(18, Pin.OUT, value=0)
in3 = Pin(19, Pin.OUT, value=0)
in4 = Pin(20, Pin.OUT, value=0)
enb = PWM(Pin(21)); enb.freq(MOTOR_PWM_FREQ); enb.duty_u16(0)

sv1 = PWM(Pin(6));  sv1.freq(SERVO_FREQ)
sv2 = PWM(Pin(7));  sv2.freq(SERVO_FREQ)
sv3 = PWM(Pin(8));  sv3.freq(SERVO_FREQ)

echo1 = Pin(9,  Pin.IN);  trig1 = Pin(10, Pin.OUT, value=0)
echo2 = Pin(11, Pin.IN);  trig2 = Pin(12, Pin.OUT, value=0)
echo3 = Pin(13, Pin.IN);  trig3 = Pin(14, Pin.OUT, value=0)

adc_moisture = ADC(Pin(26))
adc_tds      = ADC(Pin(27))

i2c    = I2C(0, sda=Pin(4), scl=Pin(5), freq=400_000)
ow_pin = Pin(2)


def _us_duty(us):
    return int(us * 65535 // SERVO_PERIOD_US)

def servo_set_us(pwm, us):
    pwm.duty_u16(_us_duty(max(500, min(2500, us))))

def servo_angle(pwm, deg):
    servo_set_us(pwm, int(1000 + (deg / 180.0) * 1000))

def servo_cw(pwm, speed=1.0):
    servo_set_us(pwm, int(1500 - speed * 500))

def servo_stop(pwm):
    servo_set_us(pwm, 1500)


def motors_forward_full():
    in1.value(1); in2.value(0)
    in3.value(1); in4.value(0)
    ena.duty_u16(MOTOR_DUTY_FULL)
    enb.duty_u16(MOTOR_DUTY_FULL)

def motors_stop():
    ena.duty_u16(0); enb.duty_u16(0)
    in1.value(0); in2.value(0)
    in3.value(0); in4.value(0)


def hcsr04_measure(trig, echo):
    trig.value(0); time.sleep_us(2)
    trig.value(1); time.sleep_us(10)
    trig.value(0)
    t0 = time.ticks_us()
    while echo.value() == 0:
        if time.ticks_diff(time.ticks_us(), t0) > HCSR04_TIMEOUT:
            return -1.0
    t1 = time.ticks_us()
    while echo.value() == 1:
        if time.ticks_diff(time.ticks_us(), t1) > HCSR04_TIMEOUT:
            return -1.0
    t2 = time.ticks_us()
    return round(time.ticks_diff(t2, t1) * SOUND_CM_PER_US, 1)

def read_all_ultrasonic():
    d1 = hcsr04_measure(trig1, echo1)
    d2 = hcsr04_measure(trig2, echo2)
    d3 = hcsr04_measure(trig3, echo3)
    valid = [(n, d) for n, d in [("Sensor-1", d1), ("Sensor-2", d2), ("Sensor-3", d3)] if d >= 0]
    if valid:
        near_name, near_dist = min(valid, key=lambda x: x[1])
    else:
        near_name, near_dist = ("None", -1.0)
    return d1, d2, d3, near_name, near_dist


def _mpu_w(reg, val):
    i2c.writeto_mem(MPU_ADDR, reg, bytes([val]))

def _mpu_r(reg, n):
    return i2c.readfrom_mem(MPU_ADDR, reg, n)

def mpu_init_and_calibrate():
    print("[MPU] Resetting ...")
    _mpu_w(MPU_PWR_MGMT_1, 0x80)
    time.sleep_ms(150)
    _mpu_w(MPU_PWR_MGMT_1, 0x00)
    time.sleep_ms(50)
    _mpu_w(MPU_SMPLRT_DIV,   0x07)
    _mpu_w(MPU_CONFIG_REG,   0x03)
    _mpu_w(MPU_GYRO_CONFIG,  0x00)
    _mpu_w(MPU_ACCEL_CONFIG, 0x00)
    who = _mpu_r(MPU_WHO_AM_I, 1)[0]
    print(f"[MPU] WHO_AM_I = 0x{who:02X}  ({'OK' if who == 0x68 else 'UNEXPECTED'})")
    print("[MPU] Calibrating - keep board STILL for 2 s ...")
    time.sleep_ms(500)
    N = 200
    sax = say = saz = sgx = sgy = sgz = 0
    for _ in range(N):
        raw = _mpu_r(MPU_ACCEL_XOUT_H, 14)
        ax, ay, az = struct.unpack(">hhh", raw[0:6])
        gx, gy, gz = struct.unpack(">hhh", raw[8:14])
        sax += ax; say += ay; saz += az
        sgx += gx; sgy += gy; sgz += gz
        time.sleep_ms(5)
    off_ax = sax // N
    off_ay = say // N
    off_az = (saz // N) - int(ACCEL_SCALE)
    off_gx = sgx // N
    off_gy = sgy // N
    off_gz = sgz // N
    print(f"[MPU] Accel offsets: ({off_ax}, {off_ay}, {off_az})")
    print(f"[MPU] Gyro  offsets: ({off_gx}, {off_gy}, {off_gz})")
    print("[MPU] Calibration done.")
    return (off_ax, off_ay, off_az), (off_gx, off_gy, off_gz)

def mpu_read(accel_off, gyro_off):
    raw = _mpu_r(MPU_ACCEL_XOUT_H, 14)
    ax_r, ay_r, az_r = struct.unpack(">hhh", raw[0:6])
    gx_r, gy_r, gz_r = struct.unpack(">hhh", raw[8:14])
    ax = (ax_r - accel_off[0]) / ACCEL_SCALE
    ay = (ay_r - accel_off[1]) / ACCEL_SCALE
    az = (az_r - accel_off[2]) / ACCEL_SCALE
    gx = (gx_r - gyro_off[0])  / GYRO_SCALE
    gy = (gy_r - gyro_off[1])  / GYRO_SCALE
    gz = (gz_r - gyro_off[2])  / GYRO_SCALE
    roll  = math.degrees(math.atan2(ay, az))
    pitch = math.degrees(math.atan2(-ax, math.sqrt(ay*ay + az*az)))
    return {
        "ax": round(ax, 3), "ay": round(ay, 3), "az": round(az, 3),
        "gx": round(gx, 2), "gy": round(gy, 2), "gz": round(gz, 2),
        "roll": round(roll, 1), "pitch": round(pitch, 1),
    }


class OneWire:
    def __init__(self, pin):
        self._p = pin

    def reset(self):
        p = self._p
        p.init(Pin.OUT); p.value(0); time.sleep_us(480)
        p.init(Pin.IN);  time.sleep_us(70)
        present = (p.value() == 0)
        time.sleep_us(410)
        return present

    def _write_bit(self, bit):
        p = self._p
        p.init(Pin.OUT); p.value(0)
        if bit:
            time.sleep_us(1);  p.init(Pin.IN); time.sleep_us(60)
        else:
            time.sleep_us(60); p.init(Pin.IN); time.sleep_us(1)

    def _read_bit(self):
        p = self._p
        p.init(Pin.OUT); p.value(0); time.sleep_us(1)
        p.init(Pin.IN);  time.sleep_us(14)
        bit = p.value()
        time.sleep_us(45)
        return bit

    def write_byte(self, byte):
        for _ in range(8):
            self._write_bit(byte & 1)
            byte >>= 1

    def read_byte(self):
        val = 0
        for i in range(8):
            val |= self._read_bit() << i
        return val

    def strong_pullup(self, ms):
        p = self._p
        p.init(Pin.OUT); p.value(1)
        time.sleep_ms(ms)
        p.init(Pin.IN)


def _ow_crc8(data):
    crc = 0
    for byte in data:
        for _ in range(8):
            mix = (crc ^ byte) & 0x01
            crc >>= 1
            if mix:
                crc ^= 0x8C
            byte >>= 1
    return crc

def ds18b20_read(ow):
    if not ow.reset():
        return -999.0
    ow.write_byte(OW_SKIP_ROM)
    ow.write_byte(OW_CONVERT_T)
    ow.strong_pullup(800)
    if not ow.reset():
        return -999.0
    ow.write_byte(OW_SKIP_ROM)
    ow.write_byte(OW_READ_SCRATCH)
    scratch = bytearray(9)
    for i in range(9):
        scratch[i] = ow.read_byte()
    if _ow_crc8(scratch) != 0:
        return -998.0
    raw = (scratch[1] << 8) | scratch[0]
    if raw == 0x0000 or raw == 0x0550:
        return -997.0
    if raw & 0x8000:
        raw -= 65536
    return round(raw / 16.0, 2)


def adc_to_v(raw):
    return raw * VREF / ADC_MAX

def voltage_to_tds(v, temp=25.0):
    comp = 1.0 + TEMP_COMP_COEFF * (temp - 25.0)
    vc   = v / comp
    tds  = (133.42 * vc**3 - 255.86 * vc**2 + 857.39 * vc) * 0.5
    return round(max(0.0, tds), 1)

def raw_to_moisture(raw):
    pct = (MOISTURE_DRY_RAW - raw) / (MOISTURE_DRY_RAW - MOISTURE_WET_RAW) * 100.0
    return round(max(0.0, min(100.0, pct)), 1)


SEP = "-" * 62

def fmt_d(d):
    return f"{d:6.1f} cm" if d >= 0 else "  NO ECHO"

def print_telemetry(n, dist, mpu, temp, tds, moist):
    d1, d2, d3, nn, nd = dist
    print(f"\n{SEP}")
    print(f"  Loop #{n:05d}")
    print(SEP)
    print("  ULTRASONIC (HC-SR04)")
    print(f"    Sensor 1  (GPIO  9/10) : {fmt_d(d1)}")
    print(f"    Sensor 2  (GPIO 11/12) : {fmt_d(d2)}")
    print(f"    Sensor 3  (GPIO 13/14) : {fmt_d(d3)}")
    if nd >= 0:
        print(f"  >> NEAREST WALL : {nn}  ->  {nd:.1f} cm")
    else:
        print("  >> NEAREST WALL : no valid reading")
    print()
    print("  MPU-6050  (SDA=GPIO4  SCL=GPIO5)")
    print(f"    Accel  X={mpu['ax']:+.3f} g   Y={mpu['ay']:+.3f} g   Z={mpu['az']:+.3f} g")
    print(f"    Gyro   X={mpu['gx']:+6.2f}/s  Y={mpu['gy']:+6.2f}/s  Z={mpu['gz']:+6.2f}/s")
    print(f"    Roll  {mpu['roll']:+6.1f}    Pitch {mpu['pitch']:+6.1f}")
    print()
    print("  DS18B20  (GPIO 2 / 1-Wire)")
    if temp > -900:
        print(f"    Temperature : {temp:.2f} C")
    elif temp == -999.0:
        print("    Temperature : *** NO DEVICE - check GPIO 2 wiring ***")
    elif temp == -998.0:
        print("    Temperature : *** CRC FAIL - check 4.7k pull-up to 3.3V ***")
    elif temp == -997.0:
        print("    Temperature : *** DEFAULT VALUE - conversion did not run ***")
    else:
        print("    Temperature : *** UNKNOWN ERROR ***")
    print()
    print("  TDS SENSOR  (GPIO 27 / ADC1)")
    print(f"    TDS : {tds:.1f} ppm")
    print()
    print("  SOIL MOISTURE  (GPIO 26 / ADC0)")
    print(f"    Moisture : {moist:.1f} %")
    print()
    print("  DC MOTORS -> FULL SPEED FORWARD  (ENA=GPIO16  ENB=GPIO21)")
    print(SEP)


def main():
    print()
    print("=" * 62)
    print("      TERRASKIPPER  -  Pico 2 W  Live Telemetry")
    print("=" * 62)

    try:
        accel_off, gyro_off = mpu_init_and_calibrate()
        mpu_ok = True
    except Exception as e:
        print(f"[MPU] INIT FAILED: {e}")
        accel_off = gyro_off = (0, 0, 0)
        mpu_ok = False

    _mpu_zero = {"ax": 0, "ay": 0, "az": 0,
                 "gx": 0, "gy": 0, "gz": 0,
                 "roll": 0, "pitch": 0}

    ow = OneWire(ow_pin)

    print("\n[MOTOR] Starting motors - full speed forward ...")
    motors_forward_full()

    servo_cw(sv1, speed=1.0)
    servo_angle(sv2, 90)
    servo_angle(sv3, 90)

    print("[DS18B20] First temperature read ...")
    last_temp  = ds18b20_read(ow)
    TEMP_EVERY = 20
    temp_ctr   = 0

    print("\n[MAIN] Entering main loop ...\n")
    loop_n = 0

    while True:
        t0 = time.ticks_ms()
        loop_n += 1

        dist_data = read_all_ultrasonic()

        if mpu_ok:
            try:
                mpu_data = mpu_read(accel_off, gyro_off)
            except Exception as e:
                print(f"[MPU] read error: {e}")
                mpu_data = _mpu_zero
        else:
            mpu_data = _mpu_zero

        temp_ctr += 1
        if temp_ctr >= TEMP_EVERY:
            temp_ctr = 0
            try:
                last_temp = ds18b20_read(ow)
            except Exception as e:
                print(f"[DS18B20] error: {e}")

        tds_v   = adc_to_v(adc_tds.read_u16())
        tds_ppm = voltage_to_tds(tds_v, temp=last_temp if last_temp > -900 else 25.0)

        moist_pct = raw_to_moisture(adc_moisture.read_u16())

        print_telemetry(loop_n, dist_data, mpu_data, last_temp, tds_ppm, moist_pct)

        wait = LOOP_PERIOD_MS - time.ticks_diff(time.ticks_ms(), t0)
        if wait > 0:
            time.sleep_ms(wait)


if __name__ == "__main__":
    main()