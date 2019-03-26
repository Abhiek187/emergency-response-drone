# HC-SR04 Code Explanation
![alt text](https://sc02.alicdn.com/kf/HTB1N.XpQVXXXXbaXVXXq6xXFXXX5/HC-SR04-HCSR04-Ultrasonic-Sensor-Wave-Detector.jpg_50x50.jpg)
## How It Works
The ultrasonic sensor, as the name implies, sends a quick pulse through the air via the trigger, in the direction that the sensor is facing. This pulse reflects off of a surface and the resulting reflected wave is then read by the 2nd sensor, the echo. The distance between the object and the sensor is thus calculated via the code. 

## Hardware
#### Purpose
The hardware aspect of the sensor depends on 4 pins on the ultrasonic sensor. Power, Ground, Trig, and Echo. 
These pins have to be connected to a Raspberry Pi so that the data that is received from using the sensor can be seen, manipulated, and used. 

#### Connectivity
The power and ground pins can be directly connected to the Pi in the appropriately allocated pins on the board. The Trig pin can also be connected directly but in an appropriate GPIO pin that can be later accessed by the Pi's terminal in Raspbian. The Echo pins have a different configuration. The pin first needs to pass through a 1k ohm resistor, and the resulting current than has to be split between a 2k ohm resistor and a wire that is connected into another GPIO pin. The reason to use resistors, is to bring down the voltage of the signal, thus not to fry the Raspberry Pi. 

##### NOTE: The resistor values can be changed based on the sensitivity of the results the user wishes to achieve.

## Software
The software of the code is explained via comments within the script. 
