#!/usr/bin/python3
# Script: Ops 401 Class 12 Ops Challenges: 
# Author: Alexander Echols.    
# Date of creation: 02 May 2023                
# Date of latest revision: 02 May 2023.      
# Purpose: add an ICMP scanner with 

# libraries
import logging
import sys
import random
# appending the scapy library to the recognized path
sys.path.append('/home/als_username/.local/lib/python3.10/site-packages')
# getting the info from scapy
from scapy.all import ICMP, IP, sr1, TCP
# Functions

def alsLogger():
# create and configure logger
    logging.basicConfig(filename="demo.log", format='%(asctime)s %(message)s', filemode='w')

        # Create the logger object
    logger = logging.getLogger()

        # Setting the threshold of logger to    DEBUG
    logger.setLevel(logging.DEBUG)

        # Test messages
    logger.debug("Just debuging, all good")
    logger.info("Just some info")
    logger.warning("Start to be concerned, this is your warning")
    logger.error("Now things are getting really bad")
    logger.critical("This is the worst it gets, good news is that it can only get better from here.")

# Global variables
# variable to hold the scanme.nmap.org DNS address
host = 'scanme.nmap.org'
# Define port range or specific set of ports to scan
port_range = [22, 23, 80, 443, 3389]
# variable to hold the network address the user wants to test
network_address = input("Enter the network address (e.g. 10.10.0.0/24): ")

# Define Functions
# function for port scanner
def Port_Scanner():
    for dst_port in port_range:
        src_port = 1025 
        # create and send the TCP SYN packet to check if the ports are open and store that in the variable 'response'
        response = sr1(IP(dst=host)/TCP(sport=src_port, dport=dst_port,flags="S"), timeout=1, verbose=0)
        # check if that response has a TCP layer and if so
        if(response.haslayer(TCP)):
            # We check if the port is open if so we...
            if(response.getlayer(TCP).flags == 0x12):
                # ...print to the screen so the user knows
                logging.info("PORT VACENT")
            # if the response is not open we...
            elif(response.getlayer(TCP).flags & 0x14 == 0x14):
                # ...print and let the user know the port is closed
                logging.info("PORT IS UNAVALABLE")
        # if there is no TCP layer indicating that the port is open or closed
        else:
            # we let the user know it is filtered and we have no idea
            print("Port is filtered mate, means we siliently drop it ")

# Function for the ICMP Scan
def ICMP_Scanner():
    # Create a list of all addresses in the given network
    network_addresses = [network_address + ip for ip in range(256)]

# Remove the network address and broadcast address from the list
    network_addresses.remove(network_address)
    network_addresses.remove(network_address + 255)

# Ping all addresses on the given network
    for network_address in network_addresses:
    # Send an ICMP echo request to the address
        response = sr1(IP(dst=network_address)/ICMP(), timeout=1, verbose=0)

    # Check if the response is received
        if response is None:
            print("Host {} is down or unresponsive.".format(network_address))
        elif response.getlayer(ICMP).type == 3 and response.getlayer(ICMP).code in [1, 2, 3, 9, 10, 13]:
            print("Host {} is actively blocking ICMP traffic.".format(network_address))
        else:
            print("Host {} is responding.".format(network_address))

# Count how many hosts are online
    online_hosts = len([network_address for network_address in network_addresses if response is not None])

    print("There are {} hosts online.".format(online_hosts))

# Main
if __name__ == '__main__':
    alsLogger()
    icmp_response = sr1(IP(dst=host)/ICMP(), timeout=1, verbose=0)

    if icmp_response is not None:
        print("Host {} is online and responding to ICMP echo requests.".format(host))
        #call Port_Scanner
        Port_Scanner()
    else:
        print("Host {} is down or unresponsive to ICMP echo requests.".format(host))
# End