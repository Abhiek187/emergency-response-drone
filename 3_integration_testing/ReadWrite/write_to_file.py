# Written and Debugged by: Abhishek Chaudhuri
# Run this in the background while testing printtest.html
import random
import time

print("Server connected")

while True:
	# Keep running until user presses Ctrl+C (or Cmd+C)
	try:
		rand_num = random.randint(1, 100)

		with open('numbers.txt', 'w') as num_file:
			num_file.write(str(rand_num)) # Write a random number into numbers.txt

		time.sleep(3)
	except KeyboardInterrupt:
		print("Server disconnected")
		break
