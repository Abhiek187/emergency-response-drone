# Emergency Response Drone (aka Search and Rescue Assistant)

This is the repo for our Software Engineering project. The Search and Rescue Assistant (or S.A.R.A.) is a drone that will help first responders find and save people trapped due to natural disasters. More info about this project can be found on [our website](https://abhiek187.github.io/emergency-response-drone). A drone is connected to a Raspberry Pi and an Android phone is used as the camera. The drone controller and camera are integrated to the website. The functions of S.A.R.A. are split between 4 subgroups:

- **image-process**: The drone is equipped with a camera that will be used to assess its surroundings and locate people in danger. It has a direct connection with the website when used with mobile devices.

- **location-data**: The location data will be used to keep track of where an emergency is taking place so S.A.R.A. can be led to the right place.

- **physical-data**: This branch deals with controlling how S.A.R.A. will move when in search and rescue mode. It will keep track of its speed, direction, power consumption, and more.

- **obstacles**: With help from its physical data, S.A.R.A. can alert users on how to respond to obstacles in its path when navigating through debris to find victims.

The project is split into 6 folders: code, unit testing, integration testing, data collection, documentation, and UML design.

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
1_code/										// Folder for source code
	about/									// Folder for about page
		custom.js 							// ???
		jquery.js 							// ???
		slide-1.jpg 						// ???
		slide-2.jpg 						// ???
		style.css 							// ???
		vegas.min.js 						// ???
		wow.min.js 							// ???
	controller/								// Folder for controller page
		Obstacles/ 							// Folder for Obstacle detection
			distance.txt 					// Test text file for storing random values
			HCSR04.py 						// Initial script to run one sensor
			leftsensor.txt 					// Text file for storing left sensor's distance in cm
			Multi-HCSR04.py 				// Initial script to run multiple sensors
			newleft_sensor.py 				// Script to run left sensor
			newright_sensor.py 				// Script to run right sensor
			rightsensor.txt 				// Text file for storing right sensor's distance in cm
		control-logic.js 					// Logic code for controller page
		control.html 						// Web file for controller page
		control_style.css 					// Styles for controler page
	README.md 								// README explaining this folder
2_unit_testing/ 							// Folder for unit testing
	Physical Data/ 							// Folder for Physical Data
		src/ 								// ???
			Velocity.java 					// Test code for how we originally planned to get speed
		.classpath 							// ???
		.gitignore 							// ???
		.project 							// ???
		Battery.html 						// Web demo for getting the battery level of device
		Controls.jar 						// ???
	README.md 								// README for unit testing
3_integration_testing/ 						// Folder for integration testing
	ReadWrite/ 								// Folder for ReadWrite tests
		numbers.txt 						// Text file for random numbers
		numGen.m 							// ???
		numtransfer.html 					// ???
		printtest.html 						// Web demo for write_to_file.py
		write_to_file.py 					// Code to write output to a text file
	cgi_test.py 							// Test code to scrape web data
	README.md 								// README for integration testing
4_data_collection/ 							// Folder for data collection
	distance.java 							// Code to calculate distance using latitude and longitude
	README.md 								// README for data collection
5_documentation/ 							// Folder for documentation
	reports/ 								// Folder for reports
		Group 8 Report1_Full.pdf 			// Full report 1
		Group 8 Report1_part1.pdf 			// Part 1 of report 1
		Group 8 Report1_part2.pdf 			// Part 2 of report 1
		Group 8 Report2_Full.pdf 			// Full report 2
		Group 8 Report2_part1.pdf 			// Part 1 of report 2
		Group 8 Report2_part2.pdf 			// Part 2 of report 2
		Group 8 Report3_Full.pdf 			// Full report 3
		Group 8 Report3_part1.pdf 			// Part 1 of report 3
	BrochureSARA.pdf 						// Brochure for 1st demo
	BrochureSARA2.pdf 						// Brochure for 2nd demo
	Group 8 contribution breakdown for demo2.xlsx // Contribution table for demo 2
	Group 8 Demo 1.pptx 					// Demo 1 presentation
	Group 8 Demo 2.pttx 					// Demo 2 presentation
	Individual Contributions (Demo 1).xlsx 	// Contribution table for demo 1
	Technical Documentation.pdf 			// Technical Documentation
	User Documentation.pdf 					// User Documentation
6_uml_design/ 								// Folder for UML diagrams (created using UMLet)
	check_obstacles.png 					// CheckObstacles sequence diagram
	class_diagram.png 						// Class diagram
	domain_model.png 						// Domain model
	get_location.png 						// GetLocation sequence diagram
	getData.png 							// GetData sequence diagram
	getStatus.png 							// GetStatus sequence diagram
	moveDrone.png 							// MoveDrone sequence diagram
	package_diagram.png 					// Package diagram
	use_case_diagram.png 					// Use case diagram
.gitattributes 								// Formatting rules for GitHub repo
index.html 									// Main web file for about page
README.md 									// The README file you're looking at!
```
For more information, please read [our technical documentation](5_documentation/technical_documentation.pdf) and [our user documentation](5_documentation/User-Documentation.pdf).
