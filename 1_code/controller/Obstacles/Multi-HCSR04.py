# Written and Debugged by: Shantanu Ghosh, Vishal Venkateswaran
import RPi.GPIO as GPIO
import time
import pigio
import sys

while True:
    try:
        GPIO.setmode(GPIO.BOARD)
        sensor1 = [7, 11]
        sensor2 = [16, 18]
        sensor3 = [33, 35]
        sensor4 = [36, 38]
        # Assigns the value of the pin position on the Pi

        GPIO.setup(sensor1[0], GPIO.OUT)
        GPIO.setup(sensor1[1], GPIO.IN)
        GPIO.setup(sensor2[0], GPIO.OUT)
        GPIO.setup(sensor2[1], GPIO.IN)
        GPIO.setup(sensor3[0], GPIO.OUT)
        GPIO.setup(sensor3[1], GPIO.IN)
        GPIO.setup(sensor4[0], GPIO.OUT)
        GPIO.setup(sensor4[1], GPIO.IN)
        '''Assigns the variables Trig and Echo to the
        appropriate I/O GPIO function.'''

        GPIO.output(sensor1[0], GPIO.LOW)
        GPIO.output(sensor2[0], GPIO.LOW)
        GPIO.output(sensor3[0], GPIO.LOW)
        GPIO.output(sensor4[0], GPIO.LOW)
        # Sets the output pin, Trig to LOW

        time.sleep(1.5)
        #Gives sensors enough time to settle before triggering again
        GPIO.output(sensor1[0], GPIO.HIGH)
        GPIO.output(sensor2[0], GPIO.HIGH)
        GPIO.output(sensor3[0], GPIO.HIGH)
        GPIO.output(sensor4[0], GPIO.HIGH)
        # Sets the output pin, Trig to HIGH

        time.sleep(0.00001)
        # A small pause of 0.01 ms

        GPIO.output(sensor1[0], GPIO.LOW)
        GPIO.output(sensor2[0], GPIO.LOW)
        GPIO.output(sensor3[0], GPIO.LOW)
        GPIO.output(sensor4[0], GPIO.LOW)
        # Resets the value of Trig to LOW

        while GPIO.input(sensor1[1])==0:
            startTime1 = time.time()
        while GPIO.input(sensor1[1])==1:
            endTime1 = time.time()

        while GPIO.input(sensor2[1])==0:
            startTime2 = time.time()
        while GPIO.input(sensor2[1])==1:
            endTime2 = time.time()

        while GPIO.input(sensor3[1])==0:
            startTime3 = time.time()
        while GPIO.input(sensor3[1])==1:
            endTime3 = time.time()

        while GPIO.input(sensor4[1])==0:
            startTime4 = time.time()
        while GPIO.input(sensor4[1])==1:
            endTime4 = time.time()
        '''Conditional statement to tell the sensor to calculate the time
        based on whether the input Echo is equal to 0 or 1.'''

        durationTime1 = endTime1 - startTime1
        durationTime2 = endTime2 - startTime2
        durationTime3 = endTime3 - startTime3
        durationTime4 = endTime4 - startTime4
        distance_L = round(durationTime1 * 17150, 2)
        distance_R = round(durationTime2 * 17150, 2)
        distance_RE = round(durationTime3 * 17150, 2)
        distance_U = round(durationTime4 * 17150, 2)
        with open('distance.txt', 'w') as num_file:
            if distance_L < 200:
                num_file.write(str("Left Distance:",distance_L/30.48,"ft"))
            elif distance_R < 200:
                num_file.write(str("Right Distance:",distance_R/30.48,"ft"))
            elif distance_RE < 200:
                num_file.write(str("Rear Distance:",distance_RE/30.48,"ft"))
            elif distance_U < 200:
                num_file.write(str("Underside Distance:",distance_U/30.48,"ft"))
            else:
                pass

        '''Calculate the total time based on the total time, and calculates the distance
        between the sensor and the measured object based on the speed of sound in one
        direction 17150 cm/s. This result is rounded to two decimal places in cm and then
        converted to feet by dividing by 30.48 and finally, returned with a prompt. This is
        done for all directions in which the sensor will be facing.'''

    finally:
        GPIO.cleanup()
        # Resets any assigned values to the pins so the code can be ran fresh again.
