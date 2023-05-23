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
import ipaddress
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
# Define Functions
# function for port scanner
def PortRangeScanner():
    host = 'scanme.nmap.org'
    port_range = [22, 23, 80, 443, 3389]
    for dst_port in port_range:
        src_port = 1025
        response = sr1(IP(dst=host) / TCP(sport=src_port, dport=dst_port, flags="S"), timeout=1, verbose=0)
        
        if response and response.haslayer(TCP):
            if response.getlayer(TCP).flags == 0x12:
                print("Port {} is open.".format(dst_port))
            elif response.getlayer(TCP).flags & 0x14 == 0x14:
                print("Port {} is closed.".format(dst_port))
        else:
            print("Port {} is filtered, status unknown.".format(dst_port))

# Function for the ICMP Scan
def icmp_scanner():
    try:
        # Prompt user for network address and subnet mask
        network_address = input("Enter the network address (e.g. 192.168.0.0/24): ")
        subnet_mask = int(input("Enter the subnet mask (e.g. 24): "))

        # Create an IP network object from the input network address
        network = ipaddress.IPv4Network(network_address)

        # Create a list of all addresses in the given network
        network_addresses = [str(ip) for ip in network.hosts()]

        # Ping all addresses on the given network
        online_hosts = 0

        for address in network_addresses:
            response = sr1(IP(dst=address) / ICMP(), timeout=1, verbose=0)

            if response is None:
                print(f"Host {address} is down or unresponsive.")
            elif response.getlayer(ICMP).type == 3 and response.getlayer(ICMP).code in [1, 2, 3, 9, 10, 13]:
                print(f"Host {address} is actively blocking ICMP traffic.")
            else:
                print(f"Host {address} is responding.")
                online_hosts += 1

        print(f"There are {online_hosts} hosts online.")

    except ValueError as e:
        print("Error: Invalid network address or subnet mask.")
    except Exception as e:
        print("Error occurred while performing ICMP scanning:", str(e))
# Main
if __name__ == '__main__':
    icmp_response = sr1(IP(dst=host)/ICMP(), timeout=1, verbose=0)

    if icmp_response is not None:
        print("Host {} is online and responding to ICMP echo requests.".format(host))
        #call Port_Scanner
        PortRangeScanner()
    else:
        print("Host {} is down or unresponsive to ICMP echo requests.".format(host))
# End