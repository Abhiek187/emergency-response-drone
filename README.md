# Emergency Response Drone (aka Search and Rescue Assistant)

This is the repo for our Software Engineering project. The Search and Rescue Assistant (or SARA) is a drone that will help first responders find and save people trapped due to natural disasters. More info about this project can be found on [our website](https://abhiek187.github.io/emergency-response-drone). The functions of SARA are split between 5 branches:

- **master**: This is the default branch for our project. All work done on other branches will be merged here and changes to the website can be made directly here.

- **image-process**: The drone is equipped with a camera that will be used to assess its surroundings and locate people in danger. It has a direct connection with the UI when used with mobile devices.

- **location-data**: The location data will be used to keep track of where an emergency is taking place so SARA can be led to the right place.

- **physical-data**: This branch deals with controlling how SARA will move when in search and rescue mode. It will keep track of its speed, direction, power consumption, and more.

- **obstacles**: With help from its physical data, SARA will know how to respond to obstacles in its path when navigating through debris to find victims.

Links to the README subfolders:
- [code](1_code/README.md)
- [unit testing](2_unit_testing/README.md)
- [integration testing](3_integration_testing/README.md)
- [data collection](4_data_collection/README.md)
