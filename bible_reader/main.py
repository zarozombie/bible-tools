# modules
import abbreviation
import bible_class

# Modules included but not needed possibally remove next revision
#import titles

"""
------------------------------------------------------------------Book Reading algorythm------------------------------------------
this portion of code is what opens books by asking user for input for specific Book (book_abrev) and Book Verse (verse) and displays scriptuer by Book and verse
"""

# flag to exit program
done = False


def main(bible_ver):
    global done
    if done == True:
        exit()
    else:
        print("-----"*10, "Welcome Select a Book", "-----"*10)
        book_abrev = input(": ")
        if book_abrev == 'q':
            done = True
            main(bible_ver)
        else:
            book_name = abbreviation.shorthand(book_abrev.lower())
            verse_inpt = input("Please Enter Verse Number: ")
            print("\n-----------------\n")
            if verse_inpt == 'q':
                done = True
                main(bible_ver)
            if type(verse_inpt) == type("is string"):
                verse_string = verse_inpt.split(":")
                if len(verse_string) < 1:
                    verse_inpt = verse_string[0]
                    verse_string = verse_string[1]
                    print(verse_string)
                print("not a verse!")
                main(bible_ver)

            else:
                ''' Legacy Code for bible_ver class update
                bible_ver = bible_class.Book(
                    book_name, verse_inpt, "", "", "", "")
                '''
                bible_ver.book = book_name
                bible_ver.verse = verse_inpt
                bookAddTxt = bible_ver.book+'.txt'
                bible_str = bible_ver.open_bk(
                    bookAddTxt, bible_ver.bookloc)  # open file in string
                ver_index = bible_ver.create_vrs_idex()  # crate verse index
                verse_index = bible_ver.index_vrs(
                    bible_str, ver_index[0], ver_index[1])  # index verse
                print(verse_index[2][0], "\n")
                bible_ver.print_verse(
                    bible_str, verse_index[0], verse_index[1], bible_ver.bookloc)  # display verse
