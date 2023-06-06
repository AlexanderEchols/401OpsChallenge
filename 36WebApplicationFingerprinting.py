#!/usr/bin/python3
# Script: Ops 401 Class 36 Ops Challenges: 
# Author: Alexander Echols.    
# Date of creation: 06 June 2023                
# Date of latest revision: 06 June 2023.      
# Purpose:
# Assisted by ChatGPT

# Libraies
import subprocess

# Functions
def netcatGrab(target, port):
    command = f"nc -v {target} {port}"
    subprocess.run(command, shell=True)

def telnetGrab(target, port):
    command = f"telnet {target, port}"
    subprocess.run(command, shell=True)

def nmapGrab(target):
    command = f"nmap -p 1-1023 -sV --script=banner {target}"
    subprocess.run(command, shell=True)

def main():
    target = input("what IP address or URL are you targeting? ")
    port = input("And the port number? ")

    netcatGrab(target, port)
    telnetGrab(target, port)
    nmapGrab(target)

main()