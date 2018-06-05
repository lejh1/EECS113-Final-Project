#############################################################################
# Filename    : Server.py
# Description : main function to run all modules 
# Author      : Jerry Lee and Justin Le
# modification: 06/01/2018
########################################################################
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

##def sendEmail(message):
##    server = smtplib.SMTP('smtp.gmail.com', 587)
##    server.starttls()
##    server.login("JujuPi2018@gmail.com", "Juju2018")
##
##    server.sendmail("JujuPi2018@gmail.com", "JujuPi2018@gmail.com", message)
##    server.quit()

def sendEmail(subject, message):
    fromaddr = "JujuPi2018@gmail.com"
    #toaddr = "JujuPi2018@gmail.com"
    toaddr = "jerrl10@uci.edu"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
     
    body = message
    msg.attach(MIMEText(body, 'plain'))
     
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "Juju2018")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    
if __name__ == '__main__':
    message = "Hello there I am JujuPi nice to meet you"
    sendEmail("HELLO WORLD", message)



 
 
