#############################################################################
# Filename    : Server.py
# Description : main function to run all modules 
# Author      : Jerry Lee and Justin Le
# modification: 06/01/2018
########################################################################
import smtplib

def sendEmail(message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("JujuPi2018@gmail.com", "Juju2018")

    server.sendmail("JujuPi2018@gmail.com", "jerrl10@uci.edu")
    server.quit()


    
