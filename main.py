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
from Server.Server import *
from Server.UserEmail import *

import time


setDistance = 0;
darkEstimate = 3;#3? need to find good standard

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
        time.sleep(5) #Give user 5 seconds to turn off security system
        if(checkSwitchMode() == 0):
            print 'intruder!!!!'
            sendEmail("Intruder Alert!", "JujuPi Security System v1.2 has detected an intruder in your household.")
            time.sleep(10) #stop checking for 10 seconds so we dont spam email    
    
if __name__ == '__main__':
    print 'Program is starting ... '
    try:
        setupMaster()
        u = UserEmail()
        setDistance = getSonar(); # set default distance for US
        print setDistance
        sendEmail("Intruder Test!")
        while True:
            #mode1
            if(checkSwitchMode()):
                LCDOn()
                while checkSwitchMode() == 1: 
                    mode1()
                    
                    #   Checks for and Temperature Requests via Email
                    emails = u.checkEmailSubjects("TEMP REQUEST") 
                    if(len(emails) > 0)
                        value = analogread(0)
                        sendEmail("Requested Temperature", str(caculateTemp(value)) + 'C')
                        u.markAsRead(emails)
                        
                    time.sleep(0.01)
            #mode2
            else :
                clearLCD()
                while checkSwitchMode() == 0:
                    mode2()

                    #   Checks for and Temperature Requests via Email
                    emails = u.checkEmailSubjects("TEMP REQUEST")
                    if(len(emails) > 0)
                        value = analogread(0)
                        sendEmail("Requested Temperature", str(caculateTemp(value)) + 'C')
                        u.markAsRead(emails)
                        
                    #   slight to give modules time to adjust
                    time.sleep(0.01)
    except KeyboardInterrupt:
        destroyMaster()
    
