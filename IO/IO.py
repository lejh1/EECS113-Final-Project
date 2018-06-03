#!/usr/bin/env python
########################################################################
# Filename    : IO.py
# Description : IO Stuff
# auther      : Justin Le
# modification: 06/02/2018
########################################################################
import RPi.GPIO as GPIO
import time

ledPinRed = 11    # RPI Board pin11 NOT GPIO
ledPinGreen = 13    # RPI Board pin5

switchPin = 15 # 

def setupIO():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(ledPinRed, GPIO.OUT)   # Set ledPinRed's mode is output
	GPIO.output(ledPinRed, GPIO.LOW) # Set ledPinRed low to off led
        GPIO.setup(ledPinGreen, GPIO.OUT)   # Set ledPinGreen's mode is output
	GPIO.output(ledPinGreen, GPIO.LOW) # Set ledPinGreen low to off led
        GPIO.setup(switchPin, GPIO.IN)   # Set ledPinGreen's mode is output

	#print 'using pin%d'%ledPin

def greenLedOn:
        GPIO.output(ledPinGreen, GPIO.HIGH)  # led on

def greenLedOff:
        GPIO.output(ledPinGreen, GPIO.LOW)  # led on

def redLedOn:
        GPIO.output(ledPinRed, GPIO.HIGH)  # led on

def redLedOff:
        GPIO.output(ledPinRed, GPIO.LOW)  # led on

def checkSwitchMode(): #Low = True = in home High= False = security
        if GPIO.input(switchPin)==GPIO.LOW:
                return True
        else :
                return False

def destroyAll():
	GPIO.output(ledPinRed, GPIO.LOW)     # led off
	GPIO.output(ledPinGreen, GPIO.LOW)     # led off
	GPIO.cleanup()                     # Release resource

