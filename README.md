# Emergency Response Drone (aka Search and Rescue Assistant)

This is the repo for our Software Engineering project. The Search and Rescue Assistant (or S.A.R.A.) is a drone that will help first responders find and save people trapped due to natural disasters. More info about this project can be found on [our website](https://abhiek187.github.io/emergency-response-drone). A drone is connected to a Raspberry Pi and an Android phone is used as the camera. The drone controller and camera are integrated to the website. The functions of S.A.R.A. are split between 4 subgroups:

- **image-process**: The drone is equipped with a camera that will be used to assess its surroundings and locate people in danger. It has a direct connection with the website when used with mobile devices.

- **location-data**: The location data will be used to keep track of where an emergency is taking place so S.A.R.A. can be led to the right place.

- **physical-data**: This branch deals with controlling how S.A.R.A. will move when in search and rescue mode. It will keep track of its speed, direction, power consumption, and more.

- **obstacles**: With help from its physical data, S.A.R.A. can alert users on how to respond to obstacles in its path when navigating through debris to find victims.

The project is split into 5 folders: code, unit testing, integration testing, data collection, and documentation.

Links to the README subfolders:
- [code](1_code/README.md)
- [unit testing](2_unit_testing/README.md)
- [integration testing](3_integration_testing/README.md)
- [data collection](4_data_collection/README.md)

## How to Run

Open [our website](https://abhiek187.github.io/emergency-response-drone) and click on _Controller_ to see S.A.R.A in action. For a local copy, [clone this repo](https://github.com/Abhiek187/emergency-response-drone.git). There are 3 components to S.A.R.A: the website, the sensors (optional), and the infared camera (optional):

### Website

Open `index.html` from this directory in your favorite browser (CTRL+O) to see the _About_ page with details about our group. The other source files can be found in the [about folder](1_code/about). Open `controller.html` in the [controller folder](1_code/controller) to see the hub for S.A.R.A. From there, you can choose your webcam, toggle the camera, see your battery level, speed, location, and sensor data (for implementation see below). Move around your device to see the speed change in real time. **Note**: you must allow your browser to use your camera and track your location.

### Sensors (optional)

To test the sensors, you will need a Raspberry Pi and two sensors connected as shown in `newleft_sensor.py` and `newright_sensor.py` in the [Obstacles folder](1_code/controller/Obstacles). Look for the PIN_TRIGGER and PIN_ECHO variables for reference. Then run those two python scripts in separate terminals, running on the Pi locally. Distance values are written into `leftsensor.txt` and `rightsensor.txt`. Next, in a third terminal, you'll need to run a python server in order for the webpage to accept fetch requests to the distance values:

1. `$ python3 newleft_sensor.py`
2. `$ python3 newright_sensor.py`
3. `$ python3 -m http.server PORT_NUM`

Then open localhost:PORT_NUM to see the sensor data update in real time. To stop the sensor scripts at any time, just press CTRL+C on that terminal window.

### Infared Camera (optional)

To see a heat map of your surroundings, you will need a [Seek Thermal Compact Camera](https://www.thermal.com/compact-series.html) as well as its corresponding app. Once configured, open the app on your smartphone for a heat map for your next emergency.

## Directory Tree
```
1_code/
	about/
		custom.js
		jquery.js
		slide-1.jpg
		slide-2.jpg
		style.css
		vegas.min.js
		wow.min.js
	controller/
		Obstacles/
			distance.txt
			HCSR04.py
			leftsensor.txt
			Multi-HCSR04.py
			newleft_sensor.py
			newright_sensor.py
			rightsensor.txt
		control-logic.js
		control.html
		control_style.css
	README.md
2_unit_testing/
	Physical Data/
		src/
			Velocity.java
		.classpath
		.gitignore
		.project
		Battery.html
		Controls.jar
	README.md
3_integration_testing/
	ReadWrite/
		numbers.txt
		numGen.m
		numtransfer.html
		printtest.html
		write_to_file.py
	cgi_test.py
	README.md
4_data_collection/
	distance.java
	README.md
5_documentation/
	reports/
		Group 8 Report1_Full.pdf
		Group 8 Report1_part1.pdf
		Group 8 Report1_part2.pdf
		Group 8 Report2_Full.pdf
		Group 8 Report2_part1.pdf
		Group 8 Report2_part2.pdf
		Group 8 Report3_Full.pdf
		Group 8 Report3_part1.pdf
	BrochureSARA.pdf
	BrochureSARA2.pdf
	Group 8 Demo 1.pptx
	Group 8 Demo 2.pttx
	Individual Contributions (Demo 1).xlsx
	technical_documentation.pdf
	User-Documentation.pdf
6_uml_design/
	domain_model.uxf
	get_location.uxf
	package_diagram.uxf
.gitattributes
index.html
README.md
```
For more information, please read [our technical documentation](5_documentation/technical_documentation.pdf) and [our user documentation](5_documentation/User-Documentation.pdf).
