import titles
import os
import abbreviation
import logging
import codecs
import bible_class

"""
------------------------------------------------------------------Book Reading algorythm------------------------------------------
this portion of code is what opens books by asking user for input for Book (book_abrev) and Book Verse (verse) and displays scriptuer by verse
"""

#flag to exit program
done = False

def main(book_loc):
    global done
    #check exit flag
    if done == True:
        exit()
    else:
#print Titles
#        if book_loc == "./KJVA":
#            titles.kjv()
#        elif book_loc == "./RSV":
#            titles.rsv()                                                                                  #disply options

# Enter Book Title/abbreciation
        print("-----"*10 , "Welcome" , "-----"*10)
        book_abrev = input("Please Enter book Name: ") 
        book_name = abbreviation.shorthand(book_abrev.lower())

        if book_name == 'q':
            done = True
            main(book_loc)
        else:
            verse_inpt = input("Please Enter Verse Number: ")

            if verse_inpt == 'q':
                done = True
                main(book_loc)

#enter Values and get outputs
            else:
                bible_ver = bible_class.Book(book_name, verse_inpt, "", "", "", "")
                book_txt = bible_ver.format_bk()                                                      #add .txt to end of file
                bible_str = bible_ver.open_bk(book_txt, book_loc)                                           #open file in string
                ver_index = bible_ver.create_vrs_idex()                                              #crate verse index
                verse_index = bible_ver.index_vrs(bible_str, ver_index[0], ver_index[1])              #index verse
                bible_ver.print_verse(bible_str, verse_index[0], verse_index[1], book_loc)                #display verse

