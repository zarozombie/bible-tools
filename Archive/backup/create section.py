import os
import re
import sys
import argparse

spanish = 'Spanish bible.txt'

os.system('cls')

f = open(spanish,"r")
string= f.read()
f.close()
slitz = string.split("Spanish Bible: ")
# os.chdir("./2")

for x in range(1,67):
    name = slitz[x]
    nametitle = name.split("\n")
    # print (len(slitz))
    # # print (slitz[2])
    # print (x , nametitle[0])
    # print (nametitle[0]+'.txt')

    print ("\"" + str(x) + " " + nametitle[0] + "\\" + "n" + "\"" "+")

    filename = nametitle[0]
    string = slitz[x]
    # f = open(filename+".txt","w+")
    # f.write(string)	 
    # f.close()


