import os
import pdb

def header():
	print('                               File             ')
	print('--------------------------------------------------------------------------')
	print('\n')
	
def footer():
	print('--------------------------------------------------------------------------')
	print('\n')
	wait2 = input("                      PRESS ENTER TO Close.")

def line():
	print('\n--------------------------------------------------------------------------\n')
#os.chdir("./Bible")

# dir_path = os.path.dirname(os.path.realpath(__file__))

# print 
# for root, dirs, files in os.walk("."):  
# 	for filename in files:
# 		print(filename)
# os.walk(directory)
# subfolders = [f.path] for f in os.scandir(folder) if f.is_dir() ] 

# Display Directorys File was exicted in
for dirs in os.walk("."):  
	print(dirs)

dir_change = input("\nWhat DIR do you want?\n")
os.chdir(dir_change)

# Print Files in Current DIR
line()
for root, dirs, files in os.walk("."):  
	for filename in files:
		print(filename)
line()


option = input("\nwhat file do you want to read?\n")
name = option

file_name = os.path.isfile(name)
# print (file_name)
# pause = input()

if (file_name == True):
	print ('this is true')
	header()
	f = open(name,'r')
	print(f.read())
	footer()

else:
	print ('this file does not exist')
	pause = input('press ENTER')
