#!/bin/python3
# Script: Ops 401 Class 06 Ops Challenges: 
# Author: Alexander Echols.    
# Date of creation: 24 April 2023                
# Date of latest revision: 24 April 2023.      
# Purpose: 
# worked with Geneva, Justin H, and Nick for help in this one.

# Libraies
from cryptography.fernet import Fernet

# Declare functions
# function to write key
def Wkey():
    key = Fernet.generate_key()
    with open("key.key", "wb").read()

# Function to load the key
def load_key():
    return open("key.key", "rb")

while True:
    chose = {
        'option 1': "Encrypt F",
        'option 2': "Decrypt F",
        'option 3': "Encrypt M",
        'option 4': "Decrypt M",
        'Exit': "Exit"
}

Make_a_choice = input("please chose fromt the following options")
