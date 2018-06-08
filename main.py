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
darkEstimate = 3; #Estimated Value for when a room has its lights off(foud via testing)

#   Cleans up GPIO and RPI when program is stopped
def destroyMaster():
    destroyLCD()
    destroyAll()
    destroyLDR()

#   Sets up all modules needed for the system
def setupMaster():
    setupUS()
    setupTemp()
    setupIO()
    setupLCD()
    setupLDR()

#   Mode 1 (In-Home-Mode)
def mode1():
    value = analogRead(0)
    #Display Time on LCD Top Row
    sendMessage1("Temp: " + str("%.2f"%abs(calculateTemp(value))) + 'C')
    #Display Time on LCD Bottom Row
    sendMessage2(get_datetime_now())

#   Mode 2 (Out-of-Home)
def mode2():
    #checks if movement or Light is detected
    if((getSonar() < ((setDistance*4)/5)) or (readLDR() < darkEstimate)):
        time.sleep(5) #Give user 5 seconds to turn off security system
        if(checkSwitchMode() == 0):
            #Send Email To Default User set in Email code (Jerry for this case)
            sendEmail("Intruder Alert!", "JujuPi Security System v1.2 has detected an intruder in your household.")
            time.sleep(10) #stop checking for 10 seconds so we dont spam email    
    
if __name__ == '__main__':
    print 'Program is starting ... '
    try:
        #   Setup Modules
        setupMaster()
        #   Setup Object for Email Reading from RPI3 Dedicated email
        u = UserEmail()
        setDistance = getSonar(); # set default distance for US

        #   On Going Loop until Keyboard detection interrupt ctrl-c
        while True:
            #   Mode 1 - checks if switch is in Mode 1
            if(checkSwitchMode()):
                LCDOn()
                while checkSwitchMode() == 1: 
                    mode1() 
                    
                    #   Checks for a Temperature Request via Email
                    emails = u.checkEmailSubjects("TEMP REQUEST") 
                    if(len(emails) > 0)
                        value = analogread(0)
                        sendEmail("Requested Temperature", str(caculateTemp(value)) + 'C')
                        u.markAsRead(emails)
                        
                    time.sleep(0.1) #slight delay for update reasons
            #   Mode 2 
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
                        
                    time.sleep(0.10)#slight delay for update reasons
                    
    #   If ctrl-c is pressed then clean up GPIO and RPI3
    except KeyboardInterrupt:
        destroyMaster()
    
