# Code

This is the source code for S.A.R.A. (besides index.html which must belong in the root of the repo).

## How to Run the Code

Open [our website](https://abhiek187.github.io/emergency-response-drone) and click on the _Controller_ tab to see the drone controller in action.

# HC-SR04 Code Explanation
![alt text](https://cdn.shopify.com/s/files/1/1978/9859/products/02_13_23_grande.jpg?v=1499266559)
## How It Works
The ultrasonic sensor, as the name implies, sends a quick pulse through the air via the trigger, in the direction that the sensor is facing. This pulse reflects off of a surface and the resulting reflected wave is then read by the 2nd sensor, the echo. The distance between the object and the sensor is thus calculated via the code.

## Hardware
#### Purpose
The hardware aspect of the sensor depends on 4 pins on the ultrasonic sensor. Power, Ground, Trig, and Echo.
These pins have to be connected to a Raspberry Pi so that the data that is received from using the sensor can be seen, manipulated, and used.

#### Connectivity
The power and ground pins can be directly connected to the Pi in the appropriately allocated pins on the board. The Trig pin can also be connected directly but in an appropriate GPIO pin that can be later accessed by the Pi's terminal in Raspbian. The Echo pins have a different configuration. The pin first needs to pass through a 1k ohm resistor, and the resulting current than has to be split between a 2k ohm resistor and a wire that is connected into another GPIO pin. The reason to use resistors, is to bring down the voltage of the signal, thus not to fry the Raspberry Pi.

## Software
The software of the code is explained via comments within the script. The _about_ folder contains code for the about section of our website and the _controller_ folder contains code for the controller section of our website (including Obstacles code). The sensor script can be found in the Obstacles folder in the python files named *newleft_sensor.py* and *newright_sensor.py*
