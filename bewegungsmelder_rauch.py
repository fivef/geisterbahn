#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

from dmx import DMX

# debounce dead time in ms
debounce_time = 5000

pir_input_pin = 18

dmx = None


def initGPIOS():

	# pin reference: GPIO uses SoC GPIO numbers not the actual pin numbers (in diagram the number after GPIO, same for both pi revisions)
	GPIO.setmode(GPIO.BCM)  

	# set pin GPIO 24 as input, enable pull down resistor
	GPIO.setup(pir_input_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)  

	#disable annoying warings
	GPIO.setwarnings(False)

# ISR
def movement_detected_callback(channel):  
	
	print "Movement detected" 

	dmx.lightening()
	#dmx.smoke()
	

  	print "Waiting for movement..."


def main():
	
	initGPIOS()

	# add interrupt on pin pir_input_pin
	GPIO.add_event_detect(pir_input_pin, GPIO.RISING, callback = movement_detected_callback, bouncetime = debounce_time) 

	global dmx

	dmx = DMX()

	print "Waiting for movement..."

	try:
    
    		while True:
        		time.sleep(1000)
	except KeyboardInterrupt:
    		GPIO.cleanup()       # clean up GPIO on CTRL+C exit
	GPIO.cleanup()           # clean up GPIO on normal exit
	

if __name__ == "__main__":
    main()
