import sys
import os
import maskpass
print ("Enter Your Login Details")
print ("")

username = input("Username:")
password = maskpass.askpass("Password:")


if username == 'admin':
  if password == 'fcbpadmin':
   start = input("Welcome... Press Enter To Start")
   print ("")
  
else:
   print ("")
   print ("Username Or Password Is Incorrect")