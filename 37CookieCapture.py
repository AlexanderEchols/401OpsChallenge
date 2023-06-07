#!/usr/bin/python3
# Script: Ops 401 Class 36 Ops Challenges: 
# Author: Alexander Echols.    
# Date of creation: 07 June 2023                
# Date of latest revision: 07 June 2023.      
# Purpose:
# Assisted by ChatGPT

# Libraries
import requests
import subprocess
# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Add here some code to make this script perform the following:
# - Send the cookie back to the site and receive a HTTP response
newResponse = requests.get(targetsite, cookies=cookie)
# - Generate a .html file to capture the contents of the HTTP response
pageContent = newResponse.text
with open("/home/als_username/401OpsChallenge/cookies.html","w") as file:
    file.write(pageContent)
# - Open it with Firefox
# first we define the path to the firefox executable
firefoxPath = '/usr/bin/firefox'
# Path to the html file
filePath = '/home/als_username/401OpsChallenge/cookies.html'
# and open with firefox
subprocess.run([firefoxPath, filePath])
# Stretch Goal
# - Give Cookie Monster hands