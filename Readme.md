# Terraskipper V2 

> A mudskipper-inspired soft robot built to help farmers monitor and understand their soil


![1.png](/Images/Full%203D%20model/Final.png)

---

## What is this?

Terraskipper is a robot that moves like a mudskipper fish. It crawls on mud and uneven ground using fins powered by DC motors and servos. While it moves around it collects soil data like pH levels, moisture, salinity and other environmental readings.

The whole idea came from a real problem. The Nile Delta in Egypt is facing serious soil degradation. Salt levels are rising and pH is shifting in ways that hurt farming. Most monitoring tools cant really reach difficult terrain or muddy areas. Terraskipper can.

The robot is designed to go where normal sensors cant and give farmers useful data about their land without them having to do much.

---

## Why I made it

I wanted to build something that actually solves a problem in the real world not just a cool robot for the sake of it. Agriculture in Egypt especially near the Nile Delta depends on soil quality and right now that soil is changing in ways that are hard to track.

A mudskipper felt like the perfect inspiration because it literally evolved to handle the transition between water and land which is exactly the kind of terrain that is hard for robots to deal with.

---

## How it works

The robot has two main systems working together

**Movement system**
- Two JGB37-520 DC Geared Motors (12V 37RPM with encoders) power the pectoral fins for forward movement
- One servo controls the caudal fin for steering and balance
- Two more servos handle the sensor placement mechanism so the sensors can move up and down to properly contact the soil

**Sensor system**
- 3x HC-SR04 ultrasonic sensors for obstacle detection and movement awareness
- MPU-6050 IMU for tilt and orientation tracking using gyroscope and accelerometer
- Ublox NEO-7M GPS module for location tracking
- Capacitive soil moisture sensor V2.0 for soil water content readings
- DS18B20 waterproof temperature sensor for soil temperature

**Brain**
- Raspberry Pi Pico 2 W handles everything
- PID control keeps the robot stable and balanced while moving
- RS485-to-TTL module for sensor communication

---

## The 3D Model

The body is split into two separate parts so it can fit inside most consumer 3D printers. The parts connect together after printing. All edges have fillets and chamfers so the robot doesnt damage the soil while crawling.

![2.png](/Images/Full%203D%20model/Untitled%20Project.png)

![2.png](/Images/Full%203D%20model/2.png)

![3.png](/Images/Full%203D%20model/3.png)



The sensor placement mechanism uses a mini linear slider with a servo motor so the sensors can move vertically and make proper contact with different soil surfaces. The mechanism is also detachable so it can be removed for repairs without taking apart the whole robot.

![3.png](/Images/Full%203D%20model/12.png)

![3.png](/Images/Full%203D%20model/14.png)

---

## PCB & Electronics

The PCB is a 2-layer board. Top layer carries signal lines and positive voltage. Bottom layer is a full GND plane to keep things clean and reduce noise.

![4.png](/Images/PCB/pcb.png)

![5.png](/Images/PCB/3d.png)

Main components on the board:

- Raspberry Pi Pico 2 W
- 2x BTS7960 43A motor drivers (one per DC motor)
- XL4016 8A and LM2596 3A buck converters for power regulation
- MPU-6050 IMU gyro and accelerometer
- Ublox NEO-7M GPS module
- Capacitive soil moisture sensor V2.0
- DS18B20 waterproof temperature sensor
- 3x HC-SR04 ultrasonic sensors

All sensors run on 3.3V logic to match the Pico 2 W. Power comes from the buck converters and sensors pull directly from the Pico 3.3V output.

---

## Wiring


![6.png](/Images/PCB/Schematic.png)

All connections go through the custom PCB. Motor drivers connect directly to the DC motors and are controlled via PWM from the Pico.

---

## Bill of Materials

18 components total. Estimated cost around **$102.50 USD / 5,315 EGP**

| Component | Category | Qty | Unit Price (EGP) | Total (EGP) |
|---|---|---|---|---|
| Raspberry Pi Pico 2 W | Microcontroller | 1 | 900 | 900 |
| BTS7960 43A DC Motor Driver | Motor Driver | 2 | 450 | 900 |
| MG996R 360° Servo Motor | Motors | 3 | 210 | 630 |
| DC Motor With Gear Box JGA25-370 12V 33RPM 30Kg.cm | Motors | 2 | 300 | 600 |
| Ublox NEO-7M GPS Module | Sensors | 1 | 540 | 540 |
| MPU-6050 IMU Gyro/Accel Module | Sensors | 1 | 175 | 175 |
| Capacitive Soil Moisture Sensor V2.0 | Sensors | 1 | 100 | 100 |
| DS18B20 Waterproof Temp Sensor | Sensors | 1 | 85 | 85 |
| HC-SR04 Ultrasonic Sensor | Sensors | 3 | 40 | 120 |
| Rechargeable Li-ion Battery Pack 18650 12V 6000mAh | Power | 1 | 900 | 900 |
| XL4016 8A Step-Down Buck Converter | Power | 1 | 243 | 243 |
| LM2596 3A Step-Down Buck Converter | Power | 1 | 122 | 122 |
| **Total** | | **18** | | **5,315 EGP** |

---

## Magazine / Zine

A project zine documenting the full design process, decisions and lessons learned is also included in this repo. It covers everything from the initial research into mudskipper locomotion to the final assembly testing.
![7.png](/Magazine/Magazine%20Terraskipper.jpg)
---

## Build Progress

The robot went through a lot of iterations. Some highlights:

- Switched from ESP32 to Raspberry Pi Pico 2 W midway through because it uses Python which is way better for me and had easier integration
- Replaced front servo motors with DC geared motors for more torque
- Rebuilt the schematic from scratch after finding SMD components weren't practical
- Redesigned the body twice to reduce filament usage and fit standard printer sizes
- Learned PID control to improve movement stability

---

## Made by

Ziad — as part of a project exploring how robotics and soft robot design can support smart farming and environmental monitoring in Egypt
