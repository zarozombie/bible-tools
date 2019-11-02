# modules
import abbreviation
import bible_class
import re
# Modules included but not needed possibally remove next revision
#import titles

"""
------------------------------------------------------------------Book Reading algorythm------------------------------------------
this portion of code is what opens books by asking user for input for specific Book (book_abrev) and Book Verse (verse) and displays scriptuer by Book and verse
"""

#flag to exit program
done = False

def main(book_loc):
    parsed_array = []

    global done
    if done == True:
        exit()
    else:


#  ==============  print Titles - Needs revision to print Books in a better format ==============
#        if book_loc == "./KJVA":
#             titles.kjv()
#        elif book_loc == "./RSV":
#             titles.rsv()

# Enter Book and verse and return Book Verse
        print("-----"*10 , "Welcome" , "-----"*10)
        book_abrev = input("What do you want to look for? ")        
        parsed_array = re.split(' |:|-', book_abrev)
        if parsed_array == 'q':
            done = True
            main(book_loc)
        else:
            book_name = abbreviation.shorthand(parsed_array[0].lower())
            try:
                bible_ver = bible_class.Book(book_name, parsed_array[1:], "", "", "", "")
            except:
                bible_ver = bible_class.Book(book_name, parsed_array, "", "", "", "")

#-----------------------TEST CODE TO BE REMOVED LATER-----------------------------
            foo = bible_ver.print_array()
            print(foo)
#-------------------------------------------------------------------

            book_txt = bible_ver.format_bk()                                                      #add .txt to end of file
            bible_str = bible_ver.open_bk(book_txt, book_loc)                                           #open file in string
            ch_index = bible_ver.create_ch_idex()                                              #crate verse index
            print(ch_index)
            verse_index = bible_ver.index_vrs(bible_str, ch_index[0], ch_index[1])              #index verse
            bible_ver.print_verse(bible_str, verse_index[0], verse_index[1], book_loc)                #display verse

