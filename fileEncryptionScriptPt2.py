#!/bin/python3
# Script: Ops 401 Class 06 Ops Challenges: 
# Author: Alexander Echols.    
# Date of creation: 25 April 2023                
# Date of latest revision: 25 April 2023.      
# Purpose: create a script 
# worked with.

# required Libraries
import os
import os.path
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

# function to encrypt a message
def message_encryption(message, key):
    plaintext = message.encode('utf-8')
    fer = Fernet(key)
    encrypted = fer.encrypt(plaintext)
    print("The encrypted message is: " + encrypted.decode('utf-8'))

# Function to decrypt a message
def message_decrypt(message_encryption, key):
    ciphertext = message_encryption.encode('utf-8')
    fer = Fernet(key)
    decrypted = fer.decrypt(ciphertext)
    print("The decrypted message is: " + decrypted.decode('utf-8'))

# Function to encrypt a file
def file_encrypt(input_file, output_file_path, output_file_name, key):
    with open(input_file, 'rb') as infile:
        plaintext = infile.read()
    encryption = Fernet(key)
    encrypt_data = encryption.encrypt(plaintext)
    output_file = output_file_path + '/' + output_file_name
    with open(output_file, 'wb') as outfile:
        outfile.write(encrypt_data)
    print(f"File successfully decrypted and saved to {output_file}")

# Function to Decrypt a file
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

# Function to encrypt the folder Recursively
def rfile_encrypt(input_path, output_path, key):
    for root, dirs, files in os.walk(input_path):
        for file in files:
            input_file = (os.path.join(root, file))
            with open(input_file, 'rb') as infile:
                plaintext = infile.read()
            encryption = Fernet(key)
            encrypt_data = encryption.encrypt(plaintext)
            output_file = (os.path.join(output_path, os.path.relpath(input_file, input_path)))
            output_dir = os.path.dirname(output_file)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            with open(output_file, 'wb') as outfile:
                outfile.write(encrypt_data)
            print(f"File {input_file} successfully encrypted and saved to {output_file}")
        for dir in dirs:
            input_dir = (os.path.join(root, dir))
            output_dir = (os.path.join(output_path, os.path.relpath(input_dir, input_path)))
        if not os.path.exists(output_dir):
                os.makedirs(output_dir)
                
# Function to Decrypt the folder Recursively
def rfile_decrypt(input_path, output_path, key):
    for root, dirs, files in os.walk(input_path):
        for file in files:
            input_file = os.path.join(root, file)
            with open(input_file, 'rb') as infile:
                encrypted_data = infile.read()
            fernet = Fernet(key)
            decrypted_data = fernet.decrypt(encrypted_data)
            output_file = os.path.join(output_path, os.path.relpath(input_file, input_path))
            output_dir = os.path.dirname(output_file)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            with open(output_file, 'wb') as outfile:
                outfile.write(decrypted_data)
            print(f'File {input_file} successfully decrypted and saved to {output_file}')
        for dir in dirs:
            input_dir = os.path.join(root, dir)
            output_dir = os.path.join(output_path, os.path.relpath(input_dir, input_path))
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            print(f"Folder {input_dir} successfully decrypted and saved to {output_dir}")


# ask the user to make a selection
# to do define main method and wrap from here down into main method
mode = input("Select what you want to do (1 = Encrypt a message, 2 = Decrypt a message, 3 = Encrypt a file, 4 = Decrypt a file, 5 = Encrypt a file recursivly, 6 = Decrypt a file recursivly, 8 = Exit): ")

if mode == '1':
    # prompt user for message to Encrypt
    message = input('What message would you like to encrypt? ')
    message_encryption(message, key)
elif mode == '2':
    encrypted_message = input("Please paste the message you wish to decrypt. ")
    message_decrypt(encrypted_message, key)
elif mode == '3':
    input_file = input("Please provide the file path to the file you wish to Encyrpt ")
    output_file_path = input("Please provide the file path for where you want the Encrypted file to be stored. ")
    output_file_name = input("What do you want to name the encripted file? ")
    file_encrypt(input_file, output_file_path,output_file_name, key)
elif mode == '4':
    input_file = input("Please provide the file path to the file you wish to decyrpt. ")
    output_file = input("Please provide the file path for where you want the decrypted file to be stored. ")
    file_decrypt(input_file, output_file, key)
elif mode == '5':
    input_path = input("Please provide the file path you wish to Encyrpt ")
    output_path = input("where do you want to put the encrypted folders? ")
    rfile_encrypt(input_path, output_path, key)
elif mode == '6':
    input_path = input("Please provide the file path you wish to Decyrpt ")
    output_path = input("where do you want to put the encrypted folders? ")
    rfile_decrypt(input_path, output_path, key)
elif mode == '8':
    print("Hope I was helpful")
    exit 