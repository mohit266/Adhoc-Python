#!/usr/bin/python3

import subprocess
import os
import crypt
user=input("Enter the user name:")
if user.isalpha()==True:
  print( "Enter username :" ,user)
else:
  print("Enter correct username")	

password="hello"+user
encryptpassword = crypt.crypt(password,"26") 
subprocess.call("useradd -p " + encryptpassword +" "+user, shell=True)
