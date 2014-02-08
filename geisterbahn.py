#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time #sleep
import smbus #i2c
import pygame #audio

UltrasonicSensorI2CAddress = 0x71

#The dead time (s) between two events.
DeadTime = 10

#If the detected distance is smaller than this value (cm) an event is triggered.
TriggerDistance = 100


# main function
def main():

  initAudio()
  DeadTimeStart = 0

  try:
    while True:
      Distance = MeasureDistance()
      print("Measured Distance = %.1f cm" % Distance)

      if Distance <= TriggerDistance and time.time() - DeadTimeStart >= DeadTime:
         DeadTimeStart = time.time()
         
         playSound()
    

  # reset GPIO settings if user pressed Ctrl+C
  except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()

def MeasureDistance():
  i2c.write_byte_data(UltrasonicSensorI2CAddress, 0, 81)
  time.sleep(0.1)
  return i2c.read_word_data(UltrasonicSensorI2CAddress, 2) / 255


def initAudio():
  pygame.mixer.init()
  pygame.mixer.music.load("sound.mp3")

def playSound():
  print("Playing sound")
  pygame.mixer.music.play()

if __name__ == '__main__':

  #init smbus 1
  i2c = smbus.SMBus(1)

  # call main function
  main()
