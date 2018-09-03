import os
import re
import sys
import argparse
# import system
spanish = 'Spanish bible.txt'

# system('cls')
os.system('cls')

# count = 0
# spanish = 'Spanish bible.txt'
# lines = [] #Declare an empty list named "lines"
# with open (spanish, 'rt') as in_file:  #Open file for reading of text data.
#     for line in in_file: #For each line of text store in a string variable named "line", and
#         lines.append(line)  #add that line to our list of lines.
# foo = lines
# foo.split()
# print(foo)
# #foo.split("Spanish Bible: ")

# with open (spanish, "r") as myfile:
    
#     data=myfile.readlines()
# data.split()
f = open(spanish,"r")
string= f.read()
f.close()
slitz = string.split("Spanish Bible: ")
name = slitz[66]
nametitle = name.split()
# print (len(slitz))
# # print (slitz[2])
# print (nametitle[0])
# x = 0
for x in range(1,67):
    name = slitz[x]
    nametitle = name.split("\n")
    # print (len(slitz))
    # # print (slitz[2])
    print (x , nametitle[0])
    # x = 0
    # print(x)


