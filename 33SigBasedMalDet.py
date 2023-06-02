#!/usr/bin/python3
# Script: Ops 401 Class 33 Ops Challenges: 
# Author: Alexander Echols.    
# Date of creation: 01 June 2023                
# Date of latest revision: 01 June 2023.      
# Purpose:
# Assisted by ChatGPT, Demo code

import hashlib
import os
import requests
from sys import platform
from datetime import datetime

# Functions
def connect():
    VTAPIkey = os.environ.get("YourKey")
    yourhash = input("What hash do you wish to check? ")
    query = 'python3 virustotal-search.py -k ' + VTAPIkey + ' -m ' + yourhash
    os.system(query)

def hashcheck(md5_hash):
    VTAPIkey = os.environ.get("YourKey")
    url = f'https://www.virustotal.com/vtapi/v2/file/report?apikey={VTAPIkey}&resource={md5_hash}'
    response = requests.get(url)
    data = response.json()
    return data

def hashfunc(filepath):
    with open(filepath, 'rb') as file:
        data = file.read()
        hashValue = hashlib.md5(data).hexdigest()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        filename = os.path.basename(filepath)
        filesize = os.path.getsize(filepath)
        print(f"{timestamp} | {filename} | {filesize} bytes | {filepath} | {hashValue}")
    return hashValue

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

def malwareDetec():
    filepath = search()
    if filepath:
        hashValue = hashfunc(filepath)
        data = hashcheck(hashValue)
        if data['response_code'] == 1:
            positives = data['positives']
            if positives > 0:
                print(f'The file is malicious. it was detected by {positives} anti-virus engines.')
            else:
                print('The file is not malicious')
        else:
            print("The file was not found on VirusTotal")

if __name__ == "__main__":
    malwareDetec()
