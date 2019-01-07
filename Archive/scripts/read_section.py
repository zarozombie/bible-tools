import os
import re
import sys
import argparse
# import system
spanish = 'Genesis.txt'

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
print(string)
# f.close()
# slitz = string.split("Spanish Bible: ")
# name = slitz[66]
# nametitle = name.split()
# print (len(slitz))
# # print (slitz[2])
# print (nametitle[0])
# x = 0
# os.chdir("./2")

# for x in range(1,67):
#     name = slitz[x]
#     nametitle = name.split("\n")
#     # print (len(slitz))
#     # # print (slitz[2])
#     print (nametitle[0]+".txt")
#     filename = nametitle[0]
#     string = slitz[x]
#     # # x = 0
    # # print(x)
    # f = open(filename+".txt","w+")
    # f.write(string)	 
    # f.close()
# os.chdir("./1")

# string = 

# f = open(filename,"w+")
# f.write(string)	 
# f.close()

# 1 Genesis
# 2 Exodus
# 3 Leviticus
# 4 Numbers
# 5 Deuteronomy
# 6 Joshua
# 7 Judges
# 8 Ruth
# 9 1 Samuel
# 10 2 Samuel
# 11 1 Kings
# 12 2 Kings
# 13 1 Chronicles
# 14 2 Chronicles
# 15 Ezra
# 16 Nehemiah
# 17 Esther
# 18 Job
# 19 Psalms
# 20 Proverbs
# 21 Ecclesiastes
# 22 Song of Solomon
# 23 Isaiah
# 24 Jeremiah
# 25 Lamentations
# 26 Ezekiel
# 27 Daniel
# 28 Hosea
# 29 Joel
# 30 Amos
# 31 Obadiah
# 32 Jonah
# 33 Micah
# 34 Nahum
# 35 Habakkuk
# 36 Zephaniah
# 37 Haggai
# 38 Zechariah
# 39 Malachi
# 40 Matthew
# 41 Mark
# 42 Luke
# 43 John
# 44 Acts
# 45 Romans
# 46 1 Corinthians
# 47 2 Corinthians
# 48 Galatians
# 49 Ephesians
# 50 Philippians
# 51 Colossians
# 52 1 Thessalonians
# 53 2 Thessalonians
# 54 1 Timothy
# 55 2 Timothy
# 56 Titus
# 57 Philemon
# 58 Hebrews
# 59 James
# 60 1 Peter
# 61 2 Peter
# 62 1 John
# 63 2 John
# 64 3 John
# 65 Jude
# 66 Revelation

# Genesis.txt
# Exodus.txt
# Leviticus.txt
# Numbers.txt
# Deuteronomy.txt
# Joshua.txt
# Judges.txt
# Ruth.txt
# 1 Samuel.txt
# 2 Samuel.txt
# 1 Kings.txt
# 2 Kings.txt
# 1 Chronicles.txt
# 2 Chronicles.txt
# Ezra.txt
# Nehemiah.txt
# Esther.txt
# Job.txt
# Psalms.txt
# Proverbs.txt
# Ecclesiastes.txt
# Song of Solomon.txt
# Isaiah.txt
# Jeremiah.txt
# Lamentations.txt
# Ezekiel.txt
# Daniel.txt
# Hosea.txt
# Joel.txt
# Amos.txt
# Obadiah.txt
# Jonah.txt
# Micah.txt
# Nahum.txt
# Habakkuk.txt
# Zephaniah.txt
# Haggai.txt
# Zechariah.txt
# Malachi.txt
# Matthew.txt
# Mark.txt
# Luke.txt
# John.txt
# Acts.txt
# Romans.txt
# 1 Corinthians.txt
# 2 Corinthians.txt
# Galatians.txt
# Ephesians.txt
# Philippians.txt
# Colossians.txt
# 1 Thessalonians.txt
# 2 Thessalonians.txt
# 1 Timothy.txt
# 2 Timothy.txt
# Titus.txt
# Philemon.txt
# Hebrews.txt
# James.txt
# 1 Peter.txt
# 2 Peter.txt
# 1 John.txt
# 2 John.txt
# 3 John.txt
# Jude.txt
# Revelation.txt