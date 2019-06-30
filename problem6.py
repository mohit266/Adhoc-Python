#!/usr/bin/python3

option='''
press 1 to display content of file
press 2 to display count of file (for cat -n command)
press 3 to overwrite the file (file > file1)
press 4 to append the file (file >> file1)
'''
print(option)

choice = input()

if choice == '1' :
	path = input("Enter Filename : ")
	file= open(file,'r')
	print(file.read())
	file.close()
elif choice == '2' :
	file= open('context.txt','r')
	count = 1
	for line in file:
           print(str(count)+line.strip())
           count+=1
elif choice == '3' :
	file=open('content.txt','r')
	path=input("Enter file name to be overwritten:")
	f2=open(path,'w')	
	f2.write(file.read())
	print(f2)
	f2.close()

elif choice == '4' :
	file=open('content.txt','r')
	file.seek(0)
	path=input("Enter the file to be apend : ")
	f2=open(path,'a')
	f2.write(file.read())
	file.close()
	f2.close()

else:
	print("Command not found")
