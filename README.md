# Emergency Response Drone (aka Search and Rescue Assistant)

This is the repo for our Software Engineering project. The Search and Rescue Assistant (or S.A.R.A.) is a drone that will help first responders find and save people trapped due to natural disasters. More info about this project can be found on [our website](https://abhiek187.github.io/emergency-response-drone). A drone is connected to a Raspberry Pi and an Android phone is used as the camera. The drone controller and camera are integrated to the website. The functions of S.A.R.A. are split between 4 subgroups:

- **image-process**: The drone is equipped with a camera that will be used to assess its surroundings and locate people in danger. It has a direct connection with the website when used with mobile devices.

- **location-data**: The location data will be used to keep track of where an emergency is taking place so S.A.R.A. can be led to the right place.

- **physical-data**: This branch deals with controlling how S.A.R.A. will move when in search and rescue mode. It will keep track of its speed, direction, power consumption, and more.

- **obstacles**: With help from its physical data, S.A.R.A. will know how to respond to obstacles in its path when navigating through debris to find victims.

The project is split into 5 folders: code, unit testing, integration testing, data collection, and documentation.

Links to the README subfolders:
- [code](1_code/README.md)
- [unit testing](2_unit_testing/README.md)
- [integration testing](3_integration_testing/README.md)
- [data collection](4_data_collection/README.md)
