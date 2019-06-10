#!/usr/bin/python3

import datetime

n = input("Enter your name :")
age = int(input("Enter your age :"))
print(n)
print(age)

d=datetime.datetime.now()
print("{} you will turn 95 by the year : {}".format(n,(95-age)+d.year))
