#!/bin/python3
# Script: Ops 401 Class 25 Ops Challenges: Uptime Sensor Part 1
# Author: Alexander Echols.    
# Date of creation: 18 April 2023                
# Date of latest revision: 18 April 2023.      
# Purpose: Write a python script that checks if a destination is up

#Main
# first we must import all the proper libraries
import time, datetime, os
# lets ask the user what address they want to check
target = input("who you checkin on?")
# next we create a Function to hold the ping
def youUp(target):
    # get the current time and store it in a variable
    ct = datetime.datetime.now()
    # Transmit a single ICMP (ping) packet to a specific IP every two seconds.
    response = os.system("ping -c 1 " + target)
    # Evaluate the response as either success or failure.
    if response == 0:
        # Assign success or failure to a status variable.
        pStatus = "We still active"
    else:
        pStatus = "No one's awake!!!!"
    print(f"{ct} {pStatus} to {target}")

# call the fuction
while True:
    youUp(target)
    time.sleep(2)
#end