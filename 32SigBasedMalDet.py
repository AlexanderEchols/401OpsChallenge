#!/usr/bin/python3
# Script: Ops 401 Class 31 Ops Challenges: 
# Author: Alexander Echols.    
# Date of creation: 30 May 2023                
# Date of latest revision: 30 May 2023.      
# Purpose:
# Assisted by democode, Serri and Bard

# Library
import hashlib
import os
from sys import platform
from datetime import datetime

# Functions
def hashfunc(filepath):
    with open(filepath, 'rb') as file:
        data = file.read()
        hashValue = hashlib.md5(data).hexdigest()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        filename = os.path.basename(filepath)
        filesize = os.path.getsize(filepath)
        print(f"{timestamp} | {filename} | {filesize} bytes | {filepath} | {hashValue}")

def search():
    whichFile = input("What file are you looking for? ")
    directory = input("What directory are we searching in? ")
    hits = 0
    searchedFiles = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == whichFile:
                hits += 1
                filepath = os.path.join(root, file)
                print(f"file found: {filepath}")
                searchedFiles += 1
                print(f"{searchedFiles} files were searched and {hits} hits were found")
                return filepath

# Main
mode = input("Do you wish to encript the files you are searching? Y/N: ")

if mode == "Y" or "y":
    filepath = search()
    if filepath:
        hashfunc(filepath)
else:
    search()
# End