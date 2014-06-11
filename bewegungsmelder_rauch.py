import RPi.GPIO as GPIO
import time
import array
from ola.ClientWrapper import ClientWrapper


Counter = 0

# debounce dead time in ms
debounce_time = 5000

pir_input_pin = 24

smoke_output_pin = 23

smoke_on_time_sec = 3

#init dmx
universe = 1


# pin reference: GPIO uses SoC GPIO numbers not the actual pin numbers (in diagram the number after GPIO, same for both pi revisions)
GPIO.setmode(GPIO.BCM)  

# set pin GPIO 24 as input, enable pull down resistor
GPIO.setup(pir_input_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)  

GPIO.setup(smoke_output_pin, GPIO.OUT)

# ISR
def Interrupt(channel):  
	
	print "Movement detected" 
	
	GPIO.output(smoke_output_pin,1)
	time.sleep(smoke_on_time_sec)
	GPIO.output(smoke_output_pin,0)
	#lightening()
	#smoke()
	

# add interrupt on pin pir_input_pin
GPIO.add_event_detect(pir_input_pin, GPIO.RISING, callback = Interrupt, bouncetime = debounce_time)   


#dmx
def DmxSent(state):
	wrapper.Stop()
	print "Dmx command successful"


def lightening():

	wrapper = ClientWrapper()
	client = wrapper.Client()

	"""B is bytecode"""
	data = array.array('B')
	data.append(255)
	data.append(255)
	data.append(255)
	data.append(255)
	data.append(255)

	client.SendDmx(universe, data)
	wrapper.Run()
	
	time.sleep(2)
	
	"""B is bytecode"""
	data = array.array('B')
	data.append(0)
	data.append(0)
	data.append(0)
	data.append(0)
	data.append(0)

	client.SendDmx(universe, data)
	wrapper.Run()
	
	wrapper.Terminate()
	
	
def smoke():

	wrapper = ClientWrapper()
	client = wrapper.Client()

	"""B is bytecode"""
	data = array.array('B')
	data.append(255)

	client.SendDmx(universe, data)
	wrapper.Run()


while True:
	time.sleep(1)
