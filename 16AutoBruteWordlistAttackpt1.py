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
    # put the path of where the password list is
    filepath = input("where are your passwords located? \n")
    # open the file
    file = open(filepath)
    line = file.readline()
    while line:
        line = line.rstrip()
        word = line
        print(word)
        time.sleep(1)
        line = file.readline()
    file.close()


def pWordCheck():
    # Accepts a user input string.
    uPWord = input("what password do you wish to check? ")
    # Accepts a user input word list file path.
    pWordList = input("what list are we testing against? ")
    # Search the word list for the user input string.
    with open(pWordList, 'r') as file:
        for line in file:
            line = line.rstrip()
            if line == uPWord:
                # Print to the screen whether the string appeared in the word list.
                print(f"Password '{uPWord}' found in list, you should change it. ")
                return
    print(f"Password '{uPWord}' not in list, good on you. ")

if mode == 1:
    iterator()
elif mode == 2:
    pWordCheck()
