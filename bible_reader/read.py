import titles
import os
import abbreviation
import logging
import codecs
import bible_class
import main

"""
----------------------------------------------------------------------Select Version---------------------------------------------------------------
this section assign oustide variables of book
"""

bible_version = input("Select Version \n 1 = KJV \n 2 = RSV \n")

if bible_version == "1":
    bible_ver = bible_class.Book("", "", 1909, "Cipriano de Valera", "Reina-Valera", "./KJVA")
elif bible_version == "2":
    bible_ver = bible_class.Book("", "", 0000, "God", "KJV", "./RSV")

#Change Directroy to location of specified bible
dir_loc = bible_ver.bookloc
os.chdir(dir_loc)

#start main Functon
main.main(bible_ver.bookloc)
