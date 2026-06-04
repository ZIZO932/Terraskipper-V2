# Terraskipper V2 — Journal Export

- Exported at: 2026-06-04T20:33:54Z
- Project ID: 3356
- Entries: 18

## Entry 1
- ID: 7011
- Author: Ziad
- Created At: 2026-05-14T02:34:59Z

### Content

For the first day, i focused on the initial research phase of the mudskipper inspired soft robot idea. i started by reviewing papers that replicate the mechanism of movement. i analyzed their fin driven locomotion, and stability on soft terrain. 

After understanding the mechanism, i shifted my research toward defining the real world problem. I investigated soil degradation issues in the Nile Delta, with a specific focus on increasing salinity levels and variations in soil pH.  

I explored available soil sensing technologies. I researched pH and TDS soil sensors and discovered an industrial-grade 7-in-1 soil sensor capable of measuring multiple environmental parameters. During this process, I learned that the sensor communicates using the RS485-to-TTL module for integration with microcontrollers.
I then researched embedded hardware options and communication between sensors and microcontrollers.

![Screenshot 2026-05-14 033001.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTUzNDksInB1ciI6ImJsb2JfaWQifX0=--432df6003cba2f941a1c831077c26313f9ada2d5/Screenshot 2026-05-14 033001.png)
![Screenshot 2026-05-14 032955.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTUzNTEsInB1ciI6ImJsb2JfaWQifX0=--d8bd7e8f48fca35160e1a759172d8c18cb04e63e/Screenshot 2026-05-14 032955.png)


### Recording Links

- https://lookout.hackclub.com/api/media/26f7359a-1249-4f7e-97dd-9e08e0848574/video.mp4

## Entry 2
- ID: 7137
- Author: Ziad
- Created At: 2026-05-14T17:35:26Z

### Content

This session took around 30 minutes and focused mainly on figuring out the movement system and starting the design.

I first looked for suitable servos for the robot since it needs to move while carrying a lot of weight from the batteries, sensors, and structure. The design needs 5 servos in total: 2 continuous (360°) for movement and 3 standard (180°) for control parts like fins and sensor movement. 

After comparing options, I found a Digital Metal Gear Servo rated at 35 kg·cm torque. It looks strong enough for the load and should handle the stress from the movement system.

After that, I started the first rough sketch of the robot body in SolidWorks. The session was short because I ran into a problem at the end.
![Screenshot 2026-05-14 203342.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU1ODcsInB1ciI6ImJsb2JfaWQifX0=--57d2116a3532f4112388309561321cf7ec3ac869/Screenshot 2026-05-14 203342.png)
![Screenshot 2026-05-14 203514.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU1OTAsInB1ciI6ImJsb2JfaWQifX0=--56a5616fc8ea7e246303c94c81297c5224915ebc/Screenshot 2026-05-14 203514.png)


### Recording Links

- https://lookout.hackclub.com/api/media/68bb0c11-6fd4-4781-b9e5-314f958a815d/video.mp4

## Entry 3
- ID: 7162
- Author: Ziad
- Created At: 2026-05-14T20:46:27Z

### Content

This session lasted about 1 hour and focused on starting the actual body design in SolidWorks.

I began by using the dimensions of the servos I selected earlier to estimate the internal layout of the robot. This helped me figure out how much space I need inside the body to properly fit all the components without overcrowding.

After that, I started shaping the main body structure and adjusted the overall dimensions to make sure it can realistically hold the full system, including servos, sensors, and electronics. The goal was to balance compact design with enough internal space for assembly and wiring.

I also added fillets and chamfers to the edges of the body design. This was important so the robot can move through soil without sharp edges damaging the ground or getting stuck, especially since it will operate in agricultural environments.

![Screenshot 2026-05-14 234449.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU2NTAsInB1ciI6ImJsb2JfaWQifX0=--7eb3fec03e6944698e4d7bb72dcb8aff7841ad42/Screenshot 2026-05-14 234449.png)
![Screenshot 2026-05-14 234500.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU2NTEsInB1ciI6ImJsb2JfaWQifX0=--61d52b1b9ac2a832ac652be8b4ee1619b5f6f429/Screenshot 2026-05-14 234500.png)


### Recording Links

- https://lookout.hackclub.com/api/media/2c941020-f8e2-43cb-abca-afc9146761ca/video.mp4

## Entry 4
- ID: 7178
- Author: Ziad
- Created At: 2026-05-14T23:51:23Z

### Content

This session took around 2 hours and was mainly focused on designing the body of the mudskipper robot in SolidWorks. I started with making the basic structure and overall shape of the body first to get an idea of how the robot would look and how the componets would fit inside.

I started using fillet and champer features on the edges so the robot doesnt damage the soil while moving and also to make the body smoother overall. Later on I noticed that some of the dimensions were not really accurate, so I remade parts of the structure again and adjusted the sizing to make more sense for the actual componets. 

I also made sure to leave a resonable amount of space inside the body for the circuit and wirings since the robot will contain multiple sensors and electronics. After that I started adding the servo holders. For the claudel fin servo, i designed a place holder and left space for the wiring and movement. I also added around 1 mm extra space to make assembly easier and avoid fitting problems later.

Then I moved to the two pectoral fin servo holders. This part took more time because the servos are placed laying down instead of standing vertically so the fitting them correctly into the body was harder. i also made sure there was enough  room for the wires and added screw holes and mounting placees for securing the servos properly.

![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU2OTUsInB1ciI6ImJsb2JfaWQifX0=--919574cd19646612808ac87aca136e91618bd5e8/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU2OTYsInB1ciI6ImJsb2JfaWQifX0=--b8348479429e30480b2865ded91baa14333bf6a4/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU2OTcsInB1ciI6ImJsb2JfaWQifX0=--0b2bf7b7c562ef4c998a6c3cf5801fc7f4fe967d/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU2OTgsInB1ciI6ImJsb2JfaWQifX0=--31ee257331ae123f5d26ce5023ec00603d491305/image.png)
![image.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTU2OTksInB1ciI6ImJsb2JfaWQifX0=--5c648192eb5bbcf169dbfca2fe5afcda07a1e345/image.png)


### Recording Links

- https://lookout.hackclub.com/api/media/58f0609b-d55e-41e4-9344-e574b6843549/video.mp4

## Entry 5
- ID: 7603
- Author: Ziad
- Created At: 2026-05-17T13:02:47Z

### Content

Todays session took around 3 hours and it was mainly about improving the body design and changing part of the movement system of the mudskipper robot.

I started by making the final changes in the body design in SolidWorks and fixing some small problems in the dimensions and spacing inside the body. While working on the design I got the idea of replacing the front servo motors with DC geared motors because they can give more torque and better continuous movement for the pectrol fins.

After that I started searching for motors that could work for the design and after comparing some options I found the JGB37-520 DC Geared Motor 12Vdc 37 RPM Complete Set With Encoder. I liked this motor because it has high torque and also comes with an encoder which can help later in controlling the movement more accuratly.

Because of changing from servos to DC motors I had to modify parts of the design again so the pectrol fins can fit and work with the new motors. This took some time because the mounting and dimensions are different from servos so I had to redesign the holders and make sure there is enough space.

After finishing the modifications I tested the body in 3D to make sure all the componets still fit correctly and there was enough room for the motors and wirings. I also checked if the body still looked compact and balanced.

At the end of the session I searched for the motor coupler that connects to the DC motor shaft so I can design the pectrol fin based on its dimensions and connection style.
![Screenshot 2026-05-17 154100.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY1ODksInB1ciI6ImJsb2JfaWQifX0=--41f7b9361b30c496ad0d6a802094f514238f70cb/Screenshot 2026-05-17 154100.png)
![Screenshot 2026-05-17 154154.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY1OTEsInB1ciI6ImJsb2JfaWQifX0=--86e12cc7dbf24f85210e2441ee299e0b2f88512c/Screenshot 2026-05-17 154154.png)
![Screenshot 2026-05-17 154210.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY1OTIsInB1ciI6ImJsb2JfaWQifX0=--053f0d4b9dbecc3dfd3d6b4f9d771afd7b3172f7/Screenshot 2026-05-17 154210.png)


### Recording Links

- https://lookout.hackclub.com/api/media/1553778a-6f36-4724-b1ba-01b956c0feac/video.mp4

## Entry 6
- ID: 7607
- Author: Ziad
- Created At: 2026-05-17T13:37:04Z

### Content

In this session the recording stopped suddenly so i was left with only 15 min in searching in the idea and how to develop a solution for this problem.
I also searched for the design that replicates the mudskipper and how to improve it.g
![Screenshot 2026-05-17 162856.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY1OTksInB1ciI6ImJsb2JfaWQifX0=--8a8360add59ac3353975f61a0062e5409d1f4343/Screenshot 2026-05-17 162856.png)


### Recording Links

- https://lookout.hackclub.com/api/media/693ef89a-bdc0-4058-b9eb-c6362b9b62e3/video.mp4

## Entry 7
- ID: 7709
- Author: Ziad
- Created At: 2026-05-18T00:57:18Z

### Content

Todays session took around 5 hours and it was mostly about fixing and improving the design of the mudskipper robot.

At first I checked the body and looked for any sharp points or edges then I added fillets to them so the robot doesnt damage the soil while moving. After that I noticed that the servo I used for the claudel fin was actually made for another servo model that was way more expensie so I changed the servo and changed the holder dimensions so it can fit the new one.

Then I started testing the body to make sure it can hold all the componets and I kept modifying the spaces and dimensions while trying different placements for the parts.

After that I used a coupler with the DC motor and started designing the pectrol fins. I designed them so they can mount on the coupler and also connect to a rod for support. Then I added fillets to the pectrol fins too so they dont damage the soil.

Later I designed the claudel fin and made it mount directly on the servo motor which actually took alot of time because I had to keep trying different dimensions and positions till it worked correctly.

At the end I spent time testing almost everything and modifying the design again until I noticed that the body was too tall compared to the rest of the 3d model so I reduced the body height to make it look more balanced.
![Screenshot 2026-05-18 035604.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY4NDMsInB1ciI6ImJsb2JfaWQifX0=--fbb1647ac266c484c427be6cf2ac266e01a8e280/Screenshot 2026-05-18 035604.png)
![Screenshot 2026-05-18 032359.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY4NDQsInB1ciI6ImJsb2JfaWQifX0=--7f32b6cd0f8783850079a14b960614094539778c/Screenshot 2026-05-18 032359.png)
![Screenshot 2026-05-17 221324.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY4NDUsInB1ciI6ImJsb2JfaWQifX0=--d041c45791390830934147f7367acc79341299e8/Screenshot 2026-05-17 221324.png)
![Screenshot 2026-05-18 032740.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY4NDYsInB1ciI6ImJsb2JfaWQifX0=--2c6edc5594046f2deaa148b3d83ea46907bb4fa4/Screenshot 2026-05-18 032740.png)
![Screenshot 2026-05-18 034531.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTY4NDcsInB1ciI6ImJsb2JfaWQifX0=--e5b38c387ce3b89fe407fced72f8ca4236a65a64/Screenshot 2026-05-18 034531.png)


### Recording Links

- https://lookout.hackclub.com/api/media/18b54523-9cce-494c-9a05-a3dec491c66c/video.mp4

## Entry 8
- ID: 7873
- Author: Ziad
- Created At: 2026-05-18T23:28:29Z

### Content

this session was mostly about trying to make the 3d model look more realistic in SolidWorks.

I started by searching how people make realistic renders for their models and found out that I need to assign materials and textures to the different parts first. When I tried doing that I noticed that the SolidWorks version I have didnt include the material and texture libraries so I had to search for how to fix that problem.

After some searching I followed a toturial that explained how to restore and add the missing libraries which took some time till it finally worked. Then I started assigning materials to the model and used soft plastic material for most of the robot parts so it can look closer to the actual design idea.

After that I followed another toturial to learn how to use SolidWorks Visualize because I never really used it before. It took a while to understand the settings lighting and camera controls but after trying different things I finally managed to render a 4K image of the model.

In the end the render actually looked pretty good and alot more realistic than the normal SolidWorks view
![Terraskipper.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTcyMTAsInB1ciI6ImJsb2JfaWQifX0=--7fe3c4d22bd389523d1b26e5677682463217473d/Terraskipper.png)


### Recording Links

- https://lookout.hackclub.com/api/media/33ebbb34-cc3e-4f22-a7eb-88939ed1059e/video.mp4

## Entry 9
- ID: 8234
- Author: Ziad
- Created At: 2026-05-20T23:44:53Z

### Content

session took around 3 and half hours and it was mainly about working on the sensor placement mechanism and how it can move up and down inside the robot.

I started by searching for different mechanisms that can move the sensors vertically and after looking through different ideas I found that using a Mini Linear Slider with a servo motor looked like the best and most effecient option for the project. After that I searched for ready made designs and tested one of the mechanisms to understand how it works and see if it would actually fit the robot.

The mechanism worked pretty well so I decided to replicate the same idea in my own design. But after checking the dimensions and mounting style I found that it wouldnt fit directly into my robot because my dimensions and holding method are different. Because of that I decided to make the whole mechanism from zero instead of copying the ready design.

After that I started designing the holder for both the servo and the linear slider in SolidWorks. While making the design I kept testing it after almost every change to make sure the movement still works correctly and the parts fit together properly.

Near the end of the session I started working on the connection between the holder and the robot body. I wanted the mechanism to be detachable so it can be removed easily later for fixing or modifications. I began designing that mounting style but I didnt fully finish it before the session ended.
![Screenshot 2026-05-21 024335.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgwMzMsInB1ciI6ImJsb2JfaWQifX0=--89aac2d4afebd9562221601725d6bcbbeab4bf5f/Screenshot 2026-05-21 024335.png)
![Screenshot 2026-05-21 024350.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTgwMzQsInB1ciI6ImJsb2JfaWQifX0=--c68b4c8ff67a30d8b417d5a79bd903524b2a02dc/Screenshot 2026-05-21 024350.png)


### Recording Links

- https://lookout.hackclub.com/api/media/4a8e292b-c036-41fc-817c-a2d1ea65d194/video.mp4

## Entry 10
- ID: 8488
- Author: Ziad
- Created At: 2026-05-22T16:19:22Z

### Content

This session was mainly about modifying the body design to fit the sensor placement mechanism.

I started by changing parts of the body so it can hold the sensor placement system correctly then I tested everything in the main assembly by placing the mechanisms on both the right and left side of the robot.

While testing I noticed that the right side needed more modification because the sensor placement caused the servo to be positioned lower than expected which could make the robot unbalanced during movement. Because of that I started working on a new version for the left sensor placement and tried different positions and dimensions.

After some testing I got the idea of mirroring the design on the y axis instead of redesigning everything from the beginning and this actually solved the balancing problem alot easier than expected.

At the end I tested the updated design again in the main assembly to make sure both sides fit correctly and the overall structure looked more balanced.
![Screenshot 2026-05-22 064835.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg1NTUsInB1ciI6ImJsb2JfaWQifX0=--3b4e34ba3c8b9103918a1a36c5b5c0941a041952/Screenshot 2026-05-22 064835.png)


### Recording Links

- https://lookout.hackclub.com/api/media/c5d7f06c-e05a-44ea-9e66-e3e51c7bb8d5/video.mp4

## Entry 11
- ID: 8598
- Author: Ziad
- Created At: 2026-05-23T05:17:42Z

### Content

I started by remaking the body because I realized that the dimensions I chose before were actually too big and would cost alot in 3d printing. I also noticed that I didnt really need all that internal space since most of it was only for the circuit. Because of that I remodeled the body with smaller dimensions.

While doing that I ran into a problem because after changing the body dimensions alot of the features and functions I already designed no longer matched correctly so I had to redo many parts again and adjust them one by one.

After that I found another issue which is that the body size was bigger than the printing area of most 3d printers. To solve this I redesigned the body into 2 seperate parts that can be placed and connected together after printing. Then I tested the new body in the main assembly and the fitting looked good.

Later I opened Ultimaker Cura and started placing each part inside the printer workspace to check the estimated filament usage and print time. I found that the body still used too much filament so I kept reducing the size little by little until I reached dimensions that looked more reasonable while still fitting the componets.

After finishing that I tested all the different models and parts together again in the main assembly to make sure everything still fits correctly after the resizing. Then I imported each part into Ultimaker again and took screenshots for documentation and checking purposes.

At the end I made sure that all the final dimensions still matched what I originally intended for the design and then created a seperate file where I documented all the dimensions along with the Ultimaker estimated print times and filament usage for each part.
![Untitled Project (4).png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg4MTcsInB1ciI6ImJsb2JfaWQifX0=--f08820d1408e1cad0bd4ee4ce5787f6e2a2259fa/Untitled Project (4).png)
![3.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg4MTgsInB1ciI6ImJsb2JfaWQifX0=--4f477baafee6c71ca6d2160644719c3287b5b4cc/3.png)
![Body part1.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg4MjAsInB1ciI6ImJsb2JfaWQifX0=--43487c643cb0c77ac19a6064287eb2ac55ed2eac/Body part1.png)
![Body part 2.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTg4MjEsInB1ciI6ImJsb2JfaWQifX0=--d23d802bc8c9f935d8d2dad58204f043bf929831/Body part 2.png)


### Recording Links

- https://lookout.hackclub.com/api/media/6fbf0e9a-73bf-41d0-a1c6-06f2eeeec6d7/video.mp4

## Entry 12
- ID: 9010
- Author: Ziad
- Created At: 2026-05-25T01:59:40Z

### Content

I started by searching for how inverted pendulem systems work and why they are commonly used in self balancing robots. After that I followed a few toturials that explained the basics of balancing and how the robot keeps itself stable while moving.

Then I started learning about PID control and how it is used to correct the balance of the robot by adjusting the motors depending on the tilt angle. I also looked into how sensors like the gyroscope and IMU work together with PID to keep the robot stable.

Most of the session was spent watching explanations and trying to understand the logic behind the balancing system since it is an important part for improving the movement and stability of the project later on.
![Screenshot 2026-05-24 004925.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTk2MTAsInB1ciI6ImJsb2JfaWQifX0=--4169249a9b0b42cc2ca4edd4a9e23a150477bb90/Screenshot 2026-05-24 004925.png)


### Recording Links

- https://lookout.hackclub.com/api/media/06aa2094-75fe-4073-9e93-9882ecd14f12/video.mp4

## Entry 13
- ID: 9190
- Author: Ziad
- Created At: 2026-05-25T20:08:02Z

### Content

I began by working on the schematic and choosing all the components that will be used in the system. I selected the main parts like the controller, sensors, motor drivers, power system, and the communication modules. While doing this I tried to make sure everything fits together and works with the requirements of the robot, especially the sensors and movement system.

After finishing the main schematic idea I started placing and connecting the components properly in the schematic so the circuit makes sense and everything is correctly powered and linked. This part took some time because I had to double check connections and make sure nothing is missing or wrong.

Then I moved to the PCB design stage. I started by assigning footprints to all the components so they can actually fit on a real board later. I checked each part carefully to make sure the footprint matches the real component size and pin layout so there wont be problems during manufacturing.

![Screenshot 2026-05-25 230726.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjAzNDksInB1ciI6ImJsb2JfaWQifX0=--a642c6448203926174634e48c542eb5a7d2f3fa5/Screenshot 2026-05-25 230726.png)


### Recording Links

- https://lookout.hackclub.com/api/media/eb1a2063-3761-40b2-b0db-2820332579e9/video.mp4

## Entry 14
- ID: 9256
- Author: Ziad
- Created At: 2026-05-26T02:56:38Z

### Content

I started by remaking the schematic because I noticed that alot of the symbols and components I used before were SMD based and that wouldnt really be practical for this project or for easier assembly and testing. Because of that I changed many of the connections into normal pins and headers so the componets can be connected and replaced easier.

While remaking the schematic I also decided to change the controller from ESP32 to the Raspberry Pi Pico 2 W because I felt it would handle the project better and also be easier for me to work with since it uses python and I already used it before in different projects. This made the programming side feel more comfortable and practical for the robot.

After finishing the new schematic I started working on the PCB again. This part took some time because I was trying to get the best placement and routing for the componets while keeping the board organized and not crowded. I kept adjusting the positions and connections until everything looked correct and cleaner.
![Screenshot 2026-05-26 041619.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjA1NDUsInB1ciI6ImJsb2JfaWQifX0=--7ee4ced3b1fb5d58d3ed86c25b3007bbf6ef73fd/Screenshot 2026-05-26 041619.png)
![Screenshot 2026-05-26 054748.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjA1NDcsInB1ciI6ImJsb2JfaWQifX0=--68f481ceb81e97c7f270ad67c5b2584c92a8d74c/Screenshot 2026-05-26 054748.png)
![Screenshot 2026-05-26 054755.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjA1NDgsInB1ciI6ImJsb2JfaWQifX0=--db079688607db9695b8abd0404a0dc000796452a/Screenshot 2026-05-26 054755.png)


### Recording Links

- https://lookout.hackclub.com/api/media/49c45843-d359-486e-a9e1-5b92491f0115/video.mp4

## Entry 15
- ID: 9834
- Author: Ziad
- Created At: 2026-05-28T04:17:17Z

### Content

This session was mostly about redoing the whole schematic because I found alot of problems in the old one. When I revisited the last schematic I noticed that many of the connections were wrong and also not really clear to understand. I also found that I was still using some SMD based parts which wouldnt be practical for the actual project.

To fix that I started remaking the schematic from the beginning and made seperate symbols for almost every sensor and board that I will actually buy and use in real life. I made the symbol and footprint for the BTS7960 motor driver and since the robot uses two DC motors I added two of them in the schematic. After that I also made symbols for the MPU sensor, GPS module, TDS sensor, soil moisture sensor and the buck converters.

After finishing the symbols and footprints I started searching for the correct connections for every sensor and module to make sure everything works properly with the Raspberry Pi Pico 2 W. This part took some time because I wanted to make sure the wiring and pins are actually correct and compatible.

I also changed the way the sensors get power. Before they were taking power from the 5 volt buck converter but after searching more I found that the Pico 2 W uses 3.3V logic signals not 5V so I changed the sensors to take power directly from the Pico 3.3V output instead to avoid problems in communication and signals.

Near the end of the session I used ERC checking to test the schematic and it found some errors and warnings so I fixed them one by one and checked again until everything finally passed correctly without problems.
![Screenshot 2026-05-28 070756.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjE4MjYsInB1ciI6ImJsb2JfaWQifX0=--654a1d393c6e0f8eba99ff862b4cdf63c5e48cc3/Screenshot 2026-05-28 070756.png)
![Screenshot 2026-05-28 065824.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjE4MjcsInB1ciI6ImJsb2JfaWQifX0=--617f8743e25609d8cf047fd415be567a0b393b3f/Screenshot 2026-05-28 065824.png)


### Recording Links

- https://lookout.hackclub.com/api/media/13396c81-535d-4534-92e0-a68a048c49ef/video.mp4

## Entry 16
- ID: 10019
- Author: Ziad
- Created At: 2026-05-29T00:27:05Z

### Content

This was mostly about remaking the PCB based on the new schematic I made before.

Most of the time went into choosing the footprints for the componets and reconnecting everything together again in the PCB. Since I changed alot in the schematic before I had to redo many parts and make sure the routing and placements still look good.

While working I noticed that I forgot to add the ultrasonic sensor in the schematic even though I want to use 3 of them for movement and obstacle detection. Because of that I went back added the symbol and footprint for it then updated the PCB again so everything fits correctly.

I also made the PCB as a 2 layer board. The first layer was mainly for the signal connections and positive voltage lines while the second layer which is the blue one was mainly used as the GND layer to make the routing cleaner and easier.

After finishing the PCB I exported it as a STEP file and added it into the main 3d model assembly to check how it fits inside the robot body. Then I tested the center of mass for the whole robot after adding all the componets and found that the balance and center of mass were actually good which means the design is looking more stable and practical.
![Screenshot 2026-05-28 204335.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjI2MzgsInB1ciI6ImJsb2JfaWQifX0=--b510edb02a8dd7cbce16108ccb49ab34e564abc4/Screenshot 2026-05-28 204335.png)
![Screenshot 2026-05-28 102245.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjI2NDAsInB1ciI6ImJsb2JfaWQifX0=--c25b38eeb32437018403a7d8459b6c7c1eeef3dd/Screenshot 2026-05-28 102245.png)


### Recording Links

- https://lookout.hackclub.com/api/media/3975db40-1db7-463f-91b7-493e4693e35c/video.mp4

## Entry 17
- ID: 10330
- Author: Ziad
- Created At: 2026-05-30T06:14:43Z

### Content

I started by looking at some toturials about how to simulate robot movement in SolidWorks and how different mates affect the motion of the assembly. After watching a few videos and understanding the basics I decided to go back to my model and remake some of the mates to make sure everything was set up correctly before running the simulation.

After that I started the simulation but I kept getting errors and the movement was not working as expected. I spent some time trying to figure out what was causing the problem and after checking different parts of the assembly I found that one of the DC motors was accidentally locked to the body which prevented the movement from happening correctly.

Once I fixed that issue I ran the simulation again but found another problem. The sensor placement mechanism was moving every time the DC motor moved even though it was supposed to stay independent from that movement. I spent some time checking the mates and connections and eventually fixed the sensor placement mechanism so it no longer moved with the motor.

By that point the main problems I found during the simulation were fixed and I decided to stop there and continue with more testing in the next session.
![Screenshot 2026-05-30 091423.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjM0MDgsInB1ciI6ImJsb2JfaWQifX0=--99722068b0ffbf73a5b2874807d9e4c24d13e27f/Screenshot 2026-05-30 091423.png)


### Recording Links

- https://lookout.hackclub.com/api/media/5896be22-fb88-4ea9-800e-112216576337/video.mp4

## Entry 18
- ID: 11702
- Author: Ziad
- Created At: 2026-06-04T20:32:49Z

### Content

 This was the longest build session which i took part in two days in which I spent the time on different parts of the project including the 3d model, BOM, coding and the magazine.

I started by making some modifications to the 3d model. The main thing I changed was the pusher of the sensor placement mechanism. I added a place for holding the sensors directly on it so the sensors can be mounted more securely and fit better with the overall design.

After that I started researching the materials and components that I am planning to use in the final prototype. I made a BOM containing all the parts and their prices. Since most of the prices were in EGP I converted them into USD to make everything easier to compare and document. While making the BOM I also tried to reduce the total cost as much as possible by comparing different options and choosing cheaper alternatives when possible without affecting the design too much.

Then I moved to the programming part of the project. I started writing the basic code for Terraskipper using Python for the Raspberry Pi Pico 2 W. This part took alot longer than I expected because I am not very experienced with programming and I had to keep searching how to control each component with the Pico. I looked up different libraries examples and documentations for the sensors motors and communication modules. Most of the time was spent understanding how everything works and making sure the code was written correctly.

After finishing the basic code I started working on the magazine. Before designing it I spent quite a while looking for inspiration and different layouts. I searched through alot of designs on Pinterest and at first I got the idea of making the magazine in a manga style inspired by Japanese manga and anime. I started creating the pages using that theme but after spending some time on it I realized I didnt really like how it looked.

Because of that I decided to start over and search for more design ideas. I looked through different styles and layouts and eventually began making a completely new design from scratch. This took the rest of the session as I kept changing things and trying different ideas until I finally reached a design that I was satisfied with.
![Magazine Terraskipper.jpg](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjcyMjIsInB1ciI6ImJsb2JfaWQifX0=--2c2d8ff220174fd43e4e5b1b23b4929279c594f5/Magazine Terraskipper.jpg)
![Screenshot 2026-06-04 233223.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjcyMjMsInB1ciI6ImJsb2JfaWQifX0=--9cabce658b2b00a9d855fe37dee58215ce96e0d0/Screenshot 2026-06-04 233223.png)
![Screenshot 2026-06-04 233153.png](/user-attachments/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MjcyMjQsInB1ciI6ImJsb2JfaWQifX0=--6236cf7cdefce2c1ce10866766b68049afb261f7/Screenshot 2026-06-04 233153.png)


### Recording Links

- https://lookout.hackclub.com/api/media/4a83534a-5144-4de7-9b66-4f9a3591fc77/video.mp4
