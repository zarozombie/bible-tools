#need to work on file

import os



dir = input ("what directory do you want to search in?\n")

#os.chdir("./1")
os.chdir(dir)

print("1 : display all files in dir and subdir")
print("2 : display files in direct dir")
print("3 : test")

choose = input("choose what function\n")



def header():
	print('                               Files in Dir             ')
	print('--------------------------------------------------------------------------')
	print('\n')
	
def footer():
	print('\n')
	print('--------------------------------------------------------------------------')
	print('\n')
	pause = input("                      PRESS ENTER TO Close.")
	

def displayeveryting():
	for root, dirs, files in os.walk("."):  
		for filename in files:
			print(filename)

def displaycurrent():
	for x in os.listdir('.'):
		print (x)
	
	
def displaypath():	
	for root, dirs, files in os.walk(".", topdown=False):
		for name in files:
			print(os.path.join(root, name))
		for name in dirs:
			print(os.path.join(root, name))
		  
if choose == "1":
	header()
	displayeveryting()
	footer()
	
elif choose =="2":
	header()
	displaycurrent()
	footer()
	
elif choose =="3":
	header()
	displaypath()
	footer()
