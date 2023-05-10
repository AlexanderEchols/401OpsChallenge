#!/usr/bin/python3
# Script: Ops 401 Class 17 Ops Challenges: 
# Author: Alexander Echols.    
# Date of creation: 09 May 2023                
# Date of latest revision: 09 May 2023.      
# Purpose: 

import paramiko
import sys, os, time
from getpass import getpass

# Mode selection
print("Choose a mode:")
print("1. Offensive; Dictionary Iterator ")
print("2. Defensive; Password Recognition ")
print("3. Conncection; SSH Connect ")

mode = int(input("Enter your choice 1, 2 or 3: "))

#function

def iterator():
    # store the path for the list of passwords
    filepath = input("where are your passwords located? \n")
    # open the file located at the filepath provided
    file = open(filepath)
    # read the first line
    line = file.readline()
    # start itirating through the full list of words
    while line:
        # formating to make it more readable
        line = line.rstrip()
        # store the read data into the variable 'line'
        word = line
        # print the stored data (or the read password)
        print(word)
        # wait for some time (1 sec) before reading the next line
        time.sleep(1)
        # read and store the next line in a variable called line
        line = file.readline()
        # if the 
    file.close()


def pWordCheck():
    # Accepts a user input string of the password they want to check
    uPWord = input("what password do you wish to check? ")
    # Accepts a user input word list file path.
    pWordList = input("what list are we testing against? ")
    # open the word list file and read its content
    with open(pWordList, 'r') as file:
        # start iterating through each line in the word list file
        for line in file:
            # Remove extra whitespace from the end of the word
            line = line.rstrip()
            # check if the users pass word that they entered above matches the word stored in line
            if line == uPWord:
                # Print to the screen whether the string appeared in the word list.
                print(f"Password '{uPWord}' found in list, you should change it. ")
                # Exit the fuction because we found a match
                return
    # and tell the user that there password is not in the list
    print(f"Password '{uPWord}' not in list, good on you. ")

def sshConnect():
    # get the ip address from the user
    host = input("what ip address are we sshing into? (ex: 192.168.5.1) ")
    # get the username from the user
    username = input("What username is being used? ")
    # get the password list from the user
    passfile = input("what is the file path to your list of passwords? ")
    # make sure the file path exists
    if os.path.exists(passfile) == False:
        print("file path doesnt exist, you should check it. ")
        sys.exit
    # start the ssh connection
    sshConnect = paramiko.SSHClient()
    # Auto-add host-key policy
    sshConnect.set_missing_host_key_policy(paramiko.AutoAddPolicy)


    try:
        # create connection 
        sshConnect.connect(host, port=22, username=username, password=passfile)
    
    except paramiko.AuthenticationException as pae:
        print("Auth failed")
        print(f"Exception occurred: {pae}")

    except KeyboardInterrupt:
        print("interruption")
        sys.exit()

# Main
if mode == 1:
    iterator()
elif mode == 2:
    pWordCheck()
elif mode == 3:
    sshConnect()