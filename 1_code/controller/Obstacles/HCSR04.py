import RPi.GPIO as GPIO
import time
while True:
	try:
 		GPIO.setmode(GPIO.BOARD)
		#assign gpio pin numbers to trigger&echo
		PIN_TRIGGER = 7
		PIN_ECHO = 11

		#assign trigger&echo to proper gpio i/o status
		GPIO.setup(PIN_TRIGGER, GPIO.OUT)
		GPIO.setup(PIN_ECHO, GPIO.IN)

		#set trigger to low
		GPIO.output(PIN_TRIGGER, GPIO.LOW)

		#prompt notification, sensor calibration
		print "Waiting for sensor to settle"
		time.sleep(2)
		print "Calculating distance"

		#set trigger to high
		GPIO.output(PIN_TRIGGER, GPIO.HIGH)
		time.sleep(0.00001)
		GPIO.output(PIN_TRIGGER, GPIO.LOW)

		#condition to set start/stop time based on echo
		while GPIO.input(PIN_ECHO)==0:
			pulse_start_time = time.time()
      		while GPIO.input(PIN_ECHO)==1:
                	pulse_end_time = time.time()

		#calculate distance based on times. assume speed of sound to  be 17150 cm/s. round distance to 2 decimal places
                pulse_duration = pulse_end_time - pulse_start_time
                distance = round(pulse_duration * 17150, 2)

		#display distance
                print "Distance:",distance,"cm"

	#allow keyboard interrupt to stop program
	except KeyboardInterrupt:
		print "Measurement stopped by User"
		GPIO.cleanup()
                break
