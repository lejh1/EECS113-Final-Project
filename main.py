#############################################################################
# Filename    : main.py
# Description : main function to run all modules 
# Author      : Jerry Lee and Justin Le
# modification: 06/01/2018
########################################################################

#from Thermometer.Thermometer.py import *
from LCD.I2CLCD1602.py import *
#from LDR.LDR.py import *
#from Ultrasonic.Ultrasonic.py import *
#from IO.IO.py import *



if __name__ == '__main__':
    print 'Program is starting ... '
    try:
        loopLCD()
    except KeyboardInterrupt:
        destroy()
