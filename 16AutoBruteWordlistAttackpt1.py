#!/usr/bin/python3


# libraries
import getpass, time, os


# file = open(filepath)


#function
'''
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
'''

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

pWordCheck()
