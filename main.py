#############################################################################
# Filename    : main.py
# Description : main function to run all modules 
# Author      : Jerry Lee and Justin Le
# modification: 06/01/2018
########################################################################

#from Thermometer.Thermometer.py import *
from LCD.I2CLCD1602 import *
#from LDR.LDR.py import *
#from Ultrasonic.Utrasonic import *
#from IO.IO.py import *



if __name__ == '__main__':
    print 'Program is starting ... '
    try:
        setupMaster()
        setupLCD()
        sendMessage("HI")
        #loopLCD()
    except KeyboardInterrupt:
        destroyMaster()

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
    
    
