#!/bin/bash

# Script: Ops 401 Lab 01.
# Author: Alexander Echols
# Date of Creation 17 April 2023
# Date of last revision: 17 April 2023
# purpose: simple script to auto update 

# Main
# lets install the Windows Update PowerShell module
Install-module -Name PSWindowsUpdate
# Import the actual module
Import-Module -Name PSWindowsUpdate
# Check for available updates
Get-WindowsUpdate
# Install all available updates
Install-WindowsUpdate -AcceptAll -AutoReboot