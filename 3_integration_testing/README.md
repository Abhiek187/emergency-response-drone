# Integration Tests Explanation

## How the Integration Tests Works
A few features from some of the subgroups are brought together and displayed on our
interface. The features include the image processing, location, battery, sensors, speed and thermal imaging.

## Features
#### Image Processing
This feature takes the camera of the given device and shows live feed of what the
camera can see.

#### Location
The location is calculated using the latitude and longitude and then displays them
on the interface.

#### Battery
This category is used to find the battery level of the device in use and then displays
the percentage value on the user interface.

#### Sensors
The sensors connected to the Raspberry Pi write distance values to a text file and is then fetched through AJAX on our website. The ReadWrite folder contains test files which have a website update every time a Python file writes a random number to the text file.

#### Speed
The calculations for speed are based on the location values found using latitude and longitude. Two consecutive location values are inputted into the Haversice formula to calculate the distance between them. This distance is then divided by the time to get speed.

#### Thermal imaging
This uses a plug-in usb thermal camera to allow the phone to see heat signatures in the environment. The seek thermal app is used to gain access to the thermal camera. 

## Software Integration
All of these features come together in the user interface which is running on the
android device. In order for the user to assess these values while the phone is in
motion, the phone screen and controls of the phone are transfered to the computer
using an app called Sidesync. As part of the integration test, the values
(camera feed, location, battery levels, sensor distance and speed) on the phone should change as the phone
is moving. Since the display on the phone changes, so to does the display on the
computer. Since Sidesync is used to view the phone screen on the computer, in order to view the thermal feed 
the user just needs to switch to the seek thermal app.The main tests involved seeing if the connection between 
the phone and the computer could be maintained. This was done in various locations and the
strength and duration of the connection depended on the wifi connection. If the
phone or computer entered an area where the wifi connection was very weak the
two devices disconnected. Basically, we found that the distance between the
phone and computer did not matter, the wifi was key for the strength of the
connection.
