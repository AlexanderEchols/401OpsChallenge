#!/usr/bin/python3
# Script: Ops 401 Class 28 Ops Challenges: 
# Author: Alexander Echols.    
# Date of creation: 24 May 2023                
# Date of latest revision: 24 May 2023.      
# Purpose: added a logger to the networkSecurityToolpt1 script 
# Assisted by ChatGPT and the Demo script

# libraries
import logging
import sys
import ipaddress
from logging.handlers import RotatingFileHandler
# appending the scapy library to the recognized path
sys.path.append('/home/als_username/.local/lib/python3.10/site-packages')
# getting the info from scapy
from scapy.all import ICMP, IP, sr1, TCP
# Functions

def alsLogger():
    # create and configure logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Set log file and rotation parameters
    logFile = 'EventLogs.log'
    maxFileSize = 500
    backCount = 3

    # Create a Stream Handler to output logs to terminal
    sHandler = logging.StreamHandler(sys.stdout)
    sHandler.setLevel(logging.WARNING)

    # Create a FileHandler to write logs to a file
    fHandler = RotatingFileHandler(logFile, maxBytes=maxFileSize, backupCount=backCount)
    fHandler.setLevel(logging.DEBUG)

    # Define log format
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    # Set the formatter for both handlers
    sHandler.setFormatter(formatter)
    fHandler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(sHandler)
    logger.addHandler(fHandler)

    # Test log messages
    logging.debug("Just debuging, all good")
    logging.info("Just some info")
    logging.warning("Start to be concerned, this is your warning")
    logging.error("Now things are getting really bad")
    logging.critical("This is the worst it gets, good news is that it can only get better from here.")

    # Intentional error to test log rotation
    try:
        result = 10 ** 1000
    except Exception as exc:
        logger.exception("an error occurred: %s", str(exc))
# Main
# Initialize and configure the logger
alsLogger()

# Define host
host = 'scanme.nmap.org'
# Define port range or specific set of ports to scan
port_range = [22, 23, 80, 443, 3389]

# start a for loop to scan all the ports in the port range
for dst_port in port_range:
    src_port = 1025
    # create and send the TCP SYN packet to check if the ports are open and store that in the variable 'response'
    try:
        # Create and send the TCP SYN packet to check if the ports are open and store the response
        response = sr1(IP(dst=host) / TCP(sport=src_port, dport=dst_port, flags="S"), timeout=1, verbose=0)

        # Check if the response is not None and has a TCP layer
        if response and response.haslayer(TCP):
            # Check if the port is open
            if response.getlayer(TCP).flags == 0x12:
                print("Port {} is open.".format(dst_port))
                logging.info("Port {} is open.".format(dst_port))
            else:
                print("Port {} is closed.".format(dst_port))
                logging.info("Port {} is closed.".format(dst_port))
        else:
            print("Port {} is filtered, status unknown.".format(dst_port))
            logging.info("Port {} is filtered, status unknown.".format(dst_port))

    except Exception as e:
        print("An error occurred while scanning port {}: {}".format(dst_port, str(e)))
        logging.error("An error occurred while scanning port {}: {}".format(dst_port, str(e)))

# End