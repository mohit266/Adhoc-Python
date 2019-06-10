#!/usr/bin/python 

import time
from googlesearch import search

f=open('link.txt','w')
web = input("pls enter topic:")
#Now time for search
for i in search(web,stop=10):
	print(i) #i only print url
	time.sleep(1)
	f.write(i)

