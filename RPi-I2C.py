from tsl2561 import TSL2561
from time import sleep


if __name__ == "__main__":
	while True:
		tsl = TSL2561(debug=True)
		x = tsl.lux()
		if(x <= 100):
			print("Too Dark: " + str(x))
		elif (x<= 200 and x>100):
			print("Dark: " + str(x))
		elif (x<= 300 and x>200):
			print("Meduim: " + str(x))
		elif (x<= 400 and x>300):
			print("Bright: " + str(x))
		elif (x<= 500 and x>400):
			print("Too Bright: " + str(x))
		sleep(2)
