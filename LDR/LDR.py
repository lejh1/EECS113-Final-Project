#!/usr/bin/env python
#############################################################################
# Filename    : LDR.py
# Description : Photoresistor control LED
# Author      : Justin Le
# modification: 06/2/2018
########################################################################
import RPi.GPIO as GPIO
import smbus
import time

address = 0x48
bus=smbus.SMBus(1)
cmd=0x40

def analogRead1(chn):
	value = bus.read_byte_data(address,cmd+chn)
	return value
	
def analogWrite(value):
	bus.write_byte_data(address,cmd,value)	

def setupLDR():
	GPIO.setmode(GPIO.BOARD)
def readLDR():
        value = analogRead1(1)
	voltage = value / 255.0 * 3.3
	return voltage
	
def loop():
	while True:
		value = analogRead1(1)
		voltage = value / 255.0 * 3.3
		print 'ADC Value : %d, Voltage : %.2f'%(value,voltage)
		time.sleep(0.01)

def destroyLDR():
	bus.close()
	
if __name__ == '__main__':
	print 'Program is starting ... '
	setupLDR()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
		
	
