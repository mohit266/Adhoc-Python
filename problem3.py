#!/usr/bin/python3

import  sys

adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]

a=[]
b=[]
while(1):
	option='''
	Press 1 To Print numbers which are greater than 5 :
	Press 2 To Print Number which are less than or equal to 2(<=2) :
	Press any key to exit 
	'''
	print(option)

	choice = input()

	if choice == '1':
			
		print("Numbers greater than 5 :")
		for i in adhoc:
			if i>5:
				print(i)
				a.append(i)
		print("list",a)

	elif choice == '2':

		print("Number which are less than or equal to 2 :")
		for i in adhoc:
			if i<=2:
				print(i)
				b.append(i)
		print("list:",b)
	

	else :
		sys.exit(0)
			
