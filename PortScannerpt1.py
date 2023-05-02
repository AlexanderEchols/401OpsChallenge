#!/usr/bin/python3
# Script: Ops 401 Class 11 Ops Challenges: 
# Author: Alexander Echols.    
# Date of creation: 01 May 2023                
# Date of latest revision: 01 May 2023.      
# Purpose: create a python script that scans ports and lets you know if they are open

# libraries
# Needed the sys library to add the location of the scapy download
import sys
# Random library for the stretch goals
import random
# appending the scapy library to the recognized path
sys.path.append('/home/als_username/.local/lib/python3.10/site-packages')
# getting the info from scapy
from scapy.all import ICMP, IP, sr1, TCP

# Main
# Define host
host = 'scanme.nmap.org'
# Define port range or specific set of ports to scan
port_range = [22, 23, 80, 443, 3389]
# start a for loop to scan all the ports in the port range
for dst_port in port_range:
    src_port = 1025 # if you want to see the stretch goal then comment out this line and...
    #src_port = random.randint(20, 3389) #... uncommint out the begening of this line
    # create and send the TCP SYN packet to check if the ports are open and store that in the variable 'response'
    response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port,flags="S"), timeout=1, verbose=0)
    # check if that response has a TCP layer and if so
    if(response.haslayer(TCP)):
        # We check if the port is open if so we...
        if(response.getlayer(TCP.flags == 0x12)):
            # ...print to the screen so the user knows
            print("PORT VACENT")
        # if the response is not open we...
        elif(response.getlayer(TCP.flags == 0x14)):
            # ...print and let the user know the port is closed
            print("PORT IS UNAVALABLE")
    # if there is no TCP layer indicating that the port is open or closed
    else:
        # we let the user know it is filtered and we have no idea
        print("Port is filtered mate, means we siliently drop it ")
# End