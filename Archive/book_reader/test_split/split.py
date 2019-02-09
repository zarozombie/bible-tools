import os, re, sys, argparse

#Load books

names_list = open("names.txt", "r")
string_name = names_list.read()
print(string_name)
print(len(string_name))
string_name_n = string_name.split("\n")
del string_name_n[-1]
print(string_name_n)
print(len(string_name))

input("Press ENTER")

os.chdir("./KJVA")
#os.system("ls")
for z in range(len(string_name)):
#        print(string[x])
    pass



#-------------------------------Production--------------------
#--------------------this code removes extra returns and------
#--------------------spaces out lines by verses in every------
#--------------------Book-------------------------------------

for c in range(len(string_name_n)):

    file_txt = string_name_n[c]
#    file_txt = "1 Corinthians.txt"
    os.system('clear')

#------------------------------open file--------
    f = open(file_txt, "r")
    string= f.read()
    f.close()

#-----------------------------Split file 
    splitz = string.split("\n")

#------------- Display split list
    string_formatting = ""

    for x in range(len(splitz)):
        string_formatting = string_formatting + splitz[x] + " "

    string_formatting = string_formatting.split("{")
    string_final = ""
    for x in range(len(string_formatting)):
        string_final = string_final + "{" + string_formatting[x] + "\n" + "\n"        

    print(string_final)

#-------------------------------- write to file----------

    f = open(string_name_n[c],"w+")
    f.write(string_final)
    f.close()  


#----------------------- iterate over bible -------------

# itereation for bible
#for x in range(1,67):
#    name = slitz[x]
#    nametitle = name.split("\n")
#    print (x , nametitle[0])

#------------------------------------------

