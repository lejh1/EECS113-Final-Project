#############################################################################
# Filename    : Server.py
# Description : main function to run all modules 
# Author      : Jerry Lee and Justin Le
# modification: 06/01/2018
########################################################################
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def sendEmail(subject, message):
    #   Email Sender address
    fromaddr = "JujuPi2018@gmail.com"
    #   Email Receiver address (using sms-to-text)
    toaddr = "16262786801@tmomail.net"	
    #toaddr = "jerrl10@uci.edu"

    #   Creating the email From, To, Body and Subject lines
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    body = message
    msg.attach(MIMEText(body, 'plain'))

    #   Using an SMTP Library to connect to our Gmail and Send the Message
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "Juju2018")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    
if __name__ == '__main__':
    message = "Hello there I am JujuPi nice to meet you"
    sendEmail("HELLO WORLD", message)



 
 
