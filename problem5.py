#!/usr/bin/python3
import datetime

name=input("Enter your name:")

current_time = datetime.datetime.now()

if current_time.hour < 12:
   print('Good morning',name)
elif 12 <= current_time.hour < 17:
   print('Good afternoon',name)
elif 16 <= current_time.hour <21:
   print('Good evening',name)
else:
   print("Goodnight",name)

