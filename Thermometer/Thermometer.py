#!/usr/bin/env python
#############################################################################
# Filename    : Thermometer.py
# Description : A DIY Thermometer
# Author      : Jerry Lee and Justin Le
# modification: 06/01/2018
########################################################################
import RPi.GPIO as GPIO
import smbus
import time
import math

address = 0x48
bus=smbus.SMBus(1)
cmd=0x40

def analogRead(chn): #used for reading value, input is pin from PCF8591
	value = bus.read_byte_data(address,cmd+chn)
	return value
	
#def analogWrite(value): 
#	bus.write_byte_data(address,cmd,value)	
	
def setup(): #setup GPIO
	GPIO.setmode(GPIO.BOARD)

def calculateTemp(value):
	voltage = value / 255.0 * 3.3		#calculate voltage
	Rt = 10 * voltage / (3.3 - voltage)	#calculate resistance value of thermistor
	tempK = 1/(1/(273.15 + 25) + math.log(Rt/10)/3950.0) #calculate temperature (Kelvin)
	tempC = tempK -273.15		#calculate temperature (Celsius)
	return tempC

def loop():
	while True:
		value = analogRead(0)		#read A0 pin		
		print 'Temperature : %.2f'%(calculateTemp)
		time.sleep(0.01)

def destroy():
	GPIO.cleanup()
	
if __name__ == '__main__':
	print 'Program is starting ... '
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
		
	
