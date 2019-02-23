# Python Libararies
import os

# Bible Modules
import bible_class
import main

#Modules included but not needed possibally remove next revision
#import titles
#import abbreviation

"""
----------------------------------------------------------------------Select Version---------------------------------------------------------------
this section determines a specific bible version and starts main module
"""

bible_version = input("Select Version \n 1 = KJV \n 2 = RSV \n")

if bible_version == "1":
    bible_ver = bible_class.Book("", "", 1909, "Cipriano de Valera", "Reina-Valera", "./KJVA")
elif bible_version == "2":
    bible_ver = bible_class.Book("", "", 0000, "God", "KJV", "./RSV")
elif bible_version == "q":
    quit()

#Change Directroy to location of specified bible
dir_loc = bible_ver.bookloc
os.chdir(dir_loc)

#start main Functon
main.main(bible_ver.bookloc)
