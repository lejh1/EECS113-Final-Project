#############################################################################
# Filename    : main.py
# Description : main function to run all modules 
# Author      : Jerry Lee and Justin Le
# modification: 06/01/2018
########################################################################

from Thermometer.Thermometer import *
from LCD.I2CLCD1602 import *
#from LDR.LDR.py import *
#from Ultrasonic.Utrasonic import *
from IO.IO import *


def destroyMaster():
    destroyLCD()
    #destroyAll()
    #destroyLDR()


def setupMaster():
   # setupUS()
    setupTemp()
    setupIO()
    setupLCD()
   # setupLDR()
    
def mode1():
    value = analogRead(0)
    sendMessage1("Temp: " + str("%.2f"%calculateTemp(value)) + 'C')
    sendMessage2(get_datetime_now())
        
if __name__ == '__main__':
    print 'Program is starting ... '
    try:
        setupMaster()
        #mode 1
        while True:
            #mode1()
            checkSwitchMode()
            sleep(0.01)
    except KeyboardInterrupt:
        destroyMaster()
    
