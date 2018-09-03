import os
import re
import sys
import argparse
# import system
spanish = 'Spanish bible.txt'

# system('cls')
os.system('cls')


def doted_line():
    print('\n\n-------------------------------------------------\n')

def padding(word):
    print('        ' + word + '\n')

def find_first_keyword(name, word):
    test = open(name, 'r').read().find(word)
    print(test)
    pause = input('Press ENTER to continue')

def fileto_string():
    count = 0
    spanish = 'Spanish bible.txt'
    lines = [] #Declare an empty list named "lines"
    with open (spanish, 'rt') as in_file:  #Open file for reading of text data.
        for line in in_file: #For each line of text store in a string variable named "line", and
            lines.append(line)  #add that line to our list of lines.
        return lines
            # print(lines[0])        #print the list object.
            # count +=1
            # print(count)        
        # print(lines[1])        #print the list object.

def strin_addr():
    spanish = 'Spanish bible.txt'
    lines = [] #Declare an empty list named "lines"
    with open (spanish, 'rt') as in_file:  #Open file lorem.txt for reading of text data.
        for line in in_file: #For each line of text store in a string variable named "line", and
            lines.append(line)  #add that line to our list of lines.
    for spanish, line in enumerate(lines):
        print(spanish, line)
    pause = input("ENTER")   

# def dis_filestring(strnumber):
def dis_filestring():
    spanish = 'Spanish bible.txt'
    lines = [] #Declare an empty list named "lines"
    with open (spanish, 'rt') as in_file:  #Open file lorem.txt for reading of text data.
        for line in in_file: #For each line of text store in a string variable named "line", and
            lines.append(line)  #add that line to our list of lines.
    return lines
            # print(lines[0])        #print the list object.

def print_line():
    spanish = 'Spanish bible.txt'
    # lines = [] #Declare an empty list named "lines"
    with open(spanish) as fin:
        fin.seek(10)
        data = fin.read(20 - 10)
        print(data)


def options_menue():
    doted_line()
    print('        1 Find first keyword\n') # find_first_keyword()
    print('        2 Assign file to string\n') # fileto_string()
    print('        3 display strin ID to fline line\n') #strin_addr()
    padding('4 display line assoc to string')
    padding('5 display 10 to 20 in str value')
    padding('6 display range of list')
    padding('7 search list')
    print('        q exit\n')
    padding("c clear") 
    doted_line()

    option = 0
    option = input ('\nWhat option do you want?\n')
    return option

def logic_system(option_v):
    if (option_v == str(1)):
        keywrd = input('What word do you want to search for\n')
        keyword = str(keywrd)
        find_first_keyword(spanish,keywrd)
        main()

    elif (option_v == str(2)):
        fileto_string()
        # pause = input("ENTER")
        main()

    elif (option_v == str(3)):
        strin_addr()
        main()

    elif (option_v == str(4)):
        number = 0
        bible = []
        bible = dis_filestring()
        number = input("\nwhat str number?\n")
        numberz = int(number)
        # display = bible[numberz]
        # print(display)
        # print(type(number))
        # print(type(4))
        # print (number)
        # print("\n" + bible)
        # print(*bible, sep='\n')
       
        print(bible[numberz])
        pause = input('press ENTER')
        main()
        
    elif (option_v == str(5)):
        print_line()
        pause = input("press ENTER")
        main()

    elif (option_v == str(6)):
        number = 0
        n = 0
        bible = []
        bible = dis_filestring()
        start = input("\nwhat str number?\n")
        startz = int(start)
        n = int(start)
        index_en = input("\nwhat str end number?\n")
        index_end = int(index_en)
        while n < index_end:
            print(bible[startz])
            startz += 1
            n += 1

        pause = input('press ENTER')
        main()
    
    elif (option_v == str(7)):
        bible = []
        bible = fileto_string()
        # search_str = input('what do you want to look for?\n')
        # index = bible.index(search_str)
        
        # print(index)
        print(bible[0])
        # for search in bible:
        #     if (search.name == search_str):
        #         test = search
        #         print(test)
        main()

    elif (option_v == 'q'):
        exit

    elif (option_v == 'c'):
        os.system('cls')
        main()   
    

def main():
    option = 0
    option = options_menue()
    logic_system(option)
    return option

option = main()

# print (option)





#search for specific keyword in file
# if 'Sacred Texts  Bible  World Bible' in open('Spanish bible.txt').read():
    #print("true")
# test = open(spanish, 'r').read().find('Spanish Bible')
# print(test)

# print(lines)
#print specific File in line
# print(lines[11])        #print the list object.





# lines = []                  # Declare an empty list named "lines"
# with open ('lorem.txt', 'rt') as in_file:  # Open file lorem.txt for reading of text data.
# for line in in_file:  # For each line of text in in_file, where the data is named "line",
# lines.append(line.rstrip('\n'))   # add that line to our list of lines, stripping newlines.
# for element in lines:            # For each element in our list,
# print(element)              # print it. 


# index = 0              # index represents where in the string we begin looking.
# str = lines[0]           # str is our string to search. In this case, lines[0].
# substr = "Spanish Bible:"            # substr is our substring for which to search. In this case, "e".
# while index < len(str): #While index is a number smaller than the number of letters in str.
#     index = str.find(substr, index) #set index to location of first remaining occurrence of "e"
#     if index == -1:         # If nothing was found,
#         break            # exit the while loop. Otherwise,
#     print("Index: ", index)     # print the index where "e" was found, and
#     index += len(substr)      # increment the index by the number of characters in substr, and repeat.

# index each line
 