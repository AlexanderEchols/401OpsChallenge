#!/bin/python3
# Script: Ops 401 Class 3 Ops Challenges: Uptime Sensor Part 2
# Author: Alexander Echols.    
# Date of creation: 19 April 2023                
# Date of latest revision: 98 April 2023.      
# Purpose: continuing the build of my uptime sensor

# Main
# Main
# first we must import all the proper libraries
import time, datetime, os
import smtplib
from getpass import getpass

# Declare variables
up = 'Network is back up and going man'
down = 'Not to worry you but, server went down!!!'
last = 0
pStatus = 0
email = input("what is your email?")
pWord = getpass("What is your password?")
target = input("what is the IP address friend?")

# Declare Functions
# Server up function
def UpAlert():
    # get the current time
    now = datetime.datetime.now()
    # create SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # authentication
    s.login(email, pWord)
    # message to send
    notification = "ITS ALIVE!!!!!! your server that is "
    # Send it
    s.sendmail("upsensore@bot.com", email, notification)
    # Terminate
    s.quit()

# server down function
def DownAlert():
    # get the current time
    now = datetime.datetime.now()
    # create SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # authentication
    s.login(email, pWord)
    # message to send
    notification = "ITS DEAD, IT'S ALL DEAD!!!!!! your server that is "
    # Send it
    s.sendmail("upsensore@bot.com", email, notification)
    # Terminate
    s.quit()

# function for ping test
def pingTest():
    global last
    global pStatus # add this line to access the global variable
    if ((pStatus != last) and (pStatus == up)):
        last = up
        UpAlert()
    elif ((pStatus != last) and (pStatus == down)):
        last = down
        DownAlert()

    # Transmit a single ICMP (ping) packet to a specific IP every two seconds.
    response = os.system("ping -c 1 " + target)
    if response == 0:
        pStatus = up
    else:
        pStatus = down


# call the fuction
while True:
    pingTest()
    time.sleep(2)
#end
