#!/bin/python3
# Script: Ops 401 Class 06 Ops Challenges: 
# Author: Alexander Echols.    
# Date of creation: 25 April 2023                
# Date of latest revision: 25 April 2023.      
# Purpose: create a script 
# worked with Geneva, Justin H, and Nick for help in this one.

# required Libraries
import os
from cryptography.fernet import Fernet

# Functions

# function to write key
def Wkey():
    # generate a key and save it to a variable called key
    key = Fernet.generate_key()
    # take the key, write it in binary, save that to a variable called "key_file"
    with open("key.key", "wb") as key_file:
        # take the key that was generated and store it in the key_file variable
        key_file.write(key)


# Function to load the key
def load_key():
    # load the key from the current file named key.key
    return open("key.key", "rb").read()

# load the previously generate key
key = load_key()

# Function to encrypt the folder
def file_encrypt(input_path, output_path, key):
    for root, dirs, files in os.walk(input_path):
        for file in files:
            input_file = os.path.join(root, file)
            with open(input_file, 'rb') as infile:
                plaintext = infile.read()
            encryption = Fernet(key)
            encrypt_data = encryption.encrypt(plaintext)
            output_file = os.path.join(output_path, os.path.relpath(input_file, input_path))
            output_dir = os.path.dirname(output_file)
            with open(output_file, 'wb') as outfile:
                outfile.write(encrypt_data)
            print(f"File {input_file} successfully encrypted and saved to {output_file}")

# Function to Decrypt the folder
def file_decrypt(input_file, output_file_dir, key):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    output_file_name = os.path.basename(input_file) + '.decrypted'
    output_file_path = os.path.join(output_file_dir, output_file_name)
    with open(output_file_path, 'wb') as file:
        file.write(decrypted_data)
    print(f"File successfully decrypted and saved to {output_file_path}")