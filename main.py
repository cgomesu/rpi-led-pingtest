#!/usr/bin/python3

# Description: A simple Python script for the RPi that blinks red/green led depending on the outome of a ping test
# Author: https://github.com/cgomesu/
# Disclaimer: The author does not provide any source of warranty

# Import needed modules
import RPi.GPIO as GPIO
import argparse
import subprocess
import time

# CLI argument parser
ap = argparse.ArgumentParser()
ap.add_argument("--redled",
				type=int,
				default=18,
				help="integer: GPIO number of the RED LED. default=18")
ap.add_argument("--greenled",
				type=int,
				default=15,
				help="integer: GPIO number of the GREEN LED. default=15")
ap.add_argument("--pinghost",
				type=str,
				default="8.8.8.8",
				help="string: host address for the ping test. default=8.8.8.8")
ap.add_argument("--pingtime",
				type=int,
				default=5,
				help="integer: ammount of time in seconds between pings. default=5")
args = vars(ap.parse_args())

# Blink LEDs
def blink_red():
	GPIO.output(args["redled"],GPIO.HIGH)
	time.sleep(.5)
	GPIO.output(args["redled"],GPIO.LOW)
	time.sleep(1)

def blink_green():
	GPIO.output(args["greenled"],GPIO.HIGH)
	time.sleep(.5)
	GPIO.output(args["greenled"],GPIO.LOW)
	time.sleep(1)

# Ping method
def ping(host):
	# Returns True if host (str) responds to a ping request
	command = ['ping', '-c', '1', host]
	return subprocess.call(command) == 0

# Configure the GPIO pins
def gpio():
	try:
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(args["redled"],GPIO.OUT)
		GPIO.setup(args["greenled"],GPIO.OUT)
		GPIO.output(args["redled"],GPIO.LOW)
		GPIO.output(args["greenled"],GPIO.LOW)
	except Exception as err:
		print('There was an error configuring the GPIO pins. Error: {}'.format(err))
		GPIO.cleanup()
		exit()

# Main
def main():
	gpio()
	while True:
		try:
			blink_green() if ping(args["pinghost"]) else blink_red()
			time.sleep(args["pingtime"])
		except:
			GPIO.cleanup()
			print('Bye!')
	

if __name__ == "__main__":
	main()
