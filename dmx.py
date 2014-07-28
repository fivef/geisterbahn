#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ola.ClientWrapper import ClientWrapper
import array
import time
#dmx

class DMX:

	universe = 1

	smoke_strength = 255
	smoke_on_time_s = 3

	def __init__(self):

		#print "Make sure the lightbar is in 5 channel mode and on channel 1"
		print "Make sure the fog machine is on channel 1"
		self.initDmx()
		

	def initDmx(self):
		self.wrapper = ClientWrapper()
		self.client = self.wrapper.Client()


	def DmxSent(self, state):

		if state.Succeeded():
			print "Sent successfully"


	def lightening(self):

		"""B is bytecode"""
		data = array.array('B')
		
		#lightbar in 5 cannel mode!!!

		data.append(255) #RED
		data.append(255) #GREEN
		data.append(255) #BLUE
		data.append(255) #BRIGHTNESS
		data.append(255) #STROBO

		self.client.SendDmx(self.universe, data, self.DmxSent)
	
		time.sleep(4)

		data = array.array('B')
		data.append(0)
		data.append(0)
		data.append(0)
		data.append(0)
		data.append(0)

		self.client.SendDmx(self.universe, data, self.DmxSent)

	
	
	def smoke(self):

		"""B is bytecode"""
		data = array.array('B')
		
		#lightbar in 5 cannel mode!!!

		data.append(self.smoke_strength) #RED
		data.append(self.smoke_strength) #GREEN
		data.append(self.smoke_strength) #BLUE
		data.append(self.smoke_strength) #BRIGHTNESS
		data.append(self.smoke_strength) #STROBO

		self.client.SendDmx(self.universe, data, self.DmxSent)
	
		time.sleep(self.smoke_on_time_s)

		data = array.array('B')
		data.append(0)
		data.append(0)
		data.append(0)
		data.append(0)
		data.append(0)

		self.client.SendDmx(self.universe, data, self.DmxSent)

		

