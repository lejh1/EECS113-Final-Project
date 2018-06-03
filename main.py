#############################################################################
# Filename    : main.py
# Description : main function to run all modules 
# Author      : Jerry Lee and Justin Le
# modification: 06/01/2018
########################################################################

from Thermometer.Thermometer import *
from LCD.I2CLCD1602 import *
#from LDR.LDR.py import *
from Ultrasonic.Utrasonic import *
from IO.IO import *
import time


setDistance = 0;

def destroyMaster():
    destroyLCD()
    destroyAll()
    destroyLDR()


def setupMaster():
    setupUS()
    setupTemp()
    setupIO()
    setupLCD()
    
def mode1():
    value = analogRead(0)
    sendMessage1("Temp: " + str("%.2f"%calculateTemp(value)) + 'C')
    sendMessage2(get_datetime_now())

def mode2():
    global setDistance
    if(getSonar < ((setDistance*4)/5):
       print 'intruder!!!!'
    
    
if __name__ == '__main__':
    print 'Program is starting ... '
    try:
        setupMaster()
        global setDistance = getSonar(); # set default distance for US
        print setDistance
        while True:
            #mode1
            if(checkSwitchMode()):
                mode1()
                time.sleep(0.01)
            #mode2
            else :
                mode2()
                time.sleep(0.01)
    except KeyboardInterrupt:
        destroyMaster()
    
