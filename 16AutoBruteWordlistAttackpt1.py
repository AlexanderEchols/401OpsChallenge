#!/usr/bin/python3
# Script: Ops 401 Class 16 Ops Challenges: 
# Author: Alexander Echols.    
# Date of creation: 08 May 2023                
# Date of latest revision: 08 May 2023.      
# Purpose: create a script to look through a list of passwords and compare them to a users input.

# libraries
import getpass, time, os


# Mode selection
print("Choose a mode:")
print("1. Offensive; Dictionary Iterator ")
print("2. Defensive; Password Recognition ")

mode = int(input("Enter your choice 1 or 2: "))


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

if mode == 1:
    iterator()
elif mode == 2:
    pWordCheck()
