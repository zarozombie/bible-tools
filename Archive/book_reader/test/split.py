import os, re, sys, argparse
# import system
os.system("ls")
file_txt = input("enter file: ")
os.system('clear')

#------------------------------open file--------
f = open(file_txt, "r")
string= f.read()
f.close()
#-----------------------------Split file 
split_char = input("what do you want to split by? ")
splitz = string.split(split_char)

#------------- Display split list
for x in range(len(splitz)):
    print("{" + splitz[x])
    print(" ")
#    print('\n')

#slitz = string.split("{")
#name = slitz[66]
#nametitle = name.split()


# itereation for bible
#for x in range(1,67):
#    name = slitz[x]
#    nametitle = name.split("\n")
#    print (x , nametitle[0])

#------------------------------------------

