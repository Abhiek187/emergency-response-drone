# Unit Tests

This is where tests are made to ensure the functions of the individual subgroups work properly.

## Unit Tests Ran

### Image Processing

The first test was made to see that the video component of the HTML loaded properly. We ran a script to have it record video from the webcam of our laptop. We had to adjust some settings to get this working on smartphones and tablets and other web browsers. Then we adjusted it so that it gets video off an Android phone as discussed in [integration testing](../3_integration_testing).

### Location Data

We also observed the latitude and longitude change in real time as we move the phone around. Since we measured location to the 5th decimal place, the changes are noticable when we move a few meters. We can also use this data to track how far we can move with the phone under a wifi signal in [data collection](../4_data_collection). This was also done using multiple devices to check for any differences in measurement.  

### Obstacles

The sensors were tested on a Raspberry Pi. The program runs in an infinite while loop as we check that the distance changes as we move obstacles of different materials and size at varying distances to test the precision of the sensor.

### Battery levels

We observed the battery level change in real time with the phone's battery. This is done through the code on the webpage.

### Thermal Imaging

For this component we used the thermal camera to test its range of detection along with its accuracy in differnt lighting environments.

### Speed

The speed is calculated using the Haversine formula. This uses 2 points on a sphere (uses latitude and longitude code) to calculate distance. We then used this distance and divided by the time it took to travel the distance to get speed. In order to test the accuracy of the speed we walked inside various buildings and drove around in our cars.
