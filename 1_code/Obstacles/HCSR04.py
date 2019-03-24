import RPi.GPIO as GPIO
import time
while True:
    try:
        GPIO.setmode(GPIO.BOARD)

        Trig = 7
        Echo = 11
        # Assigns the value of the pin position on the Pi

        GPIO.setup(Trig, GPIO.OUT)
        GPIO.setup(Echo, GPIO.IN)
        # Assigns the variables Trig and Echo to the
        # appropriate I/O GPIO function.

        GPIO.output(Trig, GPIO.LOW)
        # Sets the output pin, Trig to LOW

        print("Waiting for sensor to settle")
        time.sleep(1)
        print("Calculating distance")
        # Outputs a prompt which notifies the user that the
        # program is calculating the distance after the sensor
        # is stable enough to take a measurement.

        GPIO.output(Trig, GPIO.HIGH)
        # Sets the output pin, Trig to HIGH

        time.sleep(0.00001)
        # A small pause of 0.01 ms

        GPIO.output(Trig, GPIO.LOW)
        # Resets the value of Trig to LOW

        while GPIO.input(Echo)==0:
            startTime = time.time()
        while GPIO.input(Echo)==1:
            endTime = time.time()
        # Conditional statement to tell the sensor to calculate the time
        # based on whether the input Echo is equal to 0 or 1.

        durationTime = endTime - startTime
        distance = round(durationTime * 17150, 2)
        print("Distance:", distance,"cm")
        # Calculate the total time based on the total time, and calculates the distance
        # between the sensor and the measured object based on the speed of sound in cm in,
        # one direction 17150 cm/s. This result is rounded to two decimal places, and returned.

    finally:
        GPIO.cleanup()
        # Resets any assigned values to the pins so the code can be ran fresh again.
