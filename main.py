#############################################################################
# Filename    : main.py
# Description : main function to run all modules 
# Author      : Jerry Lee and Justin Le
# modification: 06/01/2018
########################################################################

from Thermometer.Thermometer import *
from LCD.I2CLCD1602 import *
from LDR.LDR import *
from Ultrasonic.Utrasonic import *
from IO.IO import *
import time


setDistance = 0;
darkEstimate = 2;#3? need to find good standard

def destroyMaster():
    destroyLCD()
    destroyAll()
    destroyLDR()


def setupMaster():
    setupUS()
    setupTemp()
    setupIO()
    setupLCD()
    setupLDR()

def mode1():
    value = analogRead(0)
    sendMessage1("Temp: " + str("%.2f"%abs(calculateTemp(value))) + 'C')
    sendMessage2(get_datetime_now())

def mode2():
    if((getSonar() < ((setDistance*4)/5)) or (readLDR() < darkEstimate)):
        print 'intruder!!!!'
        #need to add email stuff 
    
    
if __name__ == '__main__':
    print 'Program is starting ... '
    try:
        setupMaster()
        setDistance = getSonar(); # set default distance for US
        print setDistance
        while True:
            #mode1
            if(checkSwitchMode()):
                LCDOn()
                while checkSwitchMode() == 1: 
                    mode1()
                    time.sleep(0.01)
            #mode2
            else :
                clearLCD()
                while checkSwitchMode() == 0:
                    mode2()
                    time.sleep(0.01)
    except KeyboardInterrupt:
        destroyMaster()
    
