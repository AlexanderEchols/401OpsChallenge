#!/bin/python3
# Script: Ops 401 Class 06 Ops Challenges: 
# Author: Alexander Echols.    
# Date of creation: 24 April 2023                
# Date of latest revision: 24 April 2023.      
# Purpose: create a script 
# worked with Geneva, Justin H, and Nick for help in this one.

# Libraies
from cryptography.fernet import Fernet

# Declare functions
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
    f = Fernet(key)
    encrypted = f.encrypt(plaintext)
    print("The encrypted message is: " + encrypted.decode('utf-8'))

# Function to decrypt a message
def message_decrypt(message_encryption, key):
    ciphertext = message_encryption.encode('utf-8')
    fer = Fernet(key)
    decrypted = fer.decrypt(ciphertext)
    print("The decrypted message is: " + decrypted.decode('utf-8'))

# ask the user to make a selection
mode = input("Select what you want to do (1 = Encrypt a message, 2 = Decrypt a message, 3 = Encrypt a file, 4 = Decrypt a file): ")

if mode == '1':
    # prompt user for message to Encrypt
    message = input('what message would you like to encrypt? ').encode()
    message_encryption()
elif mode == '2':
    message_decrypt()
elif mode == '3':

elif mode == '4':

elif mode == '5':
    print("Hope I was helpful")
    break


# Initialize the Fernet class
#encryption = Fernet(key)

# message encryption
#encrypted = encryption.encrypt(message)

# print the encrypted message
#print("The encrypted message is " + encrypted.decode('utf-8'))


# Start the decryption
#decryption = Fernet(key)

#decrypted = decryption.decrypt(encrypted)
#print("The decrypted message is " + decrypted.decode('utf-8'))
