import random
import time

print("Server connected")

while True:
	try:
		rand_num = random.randint(1, 100)

		with open('numbers.txt', 'w') as num_file:
			num_file.write(str(rand_num))

		time.sleep(3)
	except KeyboardInterrupt:
		print("Server disconnected")
		break
