import titles
import os
import abbreviation
import logging
import codecs


"""
------------------------------------------------------------------Book Reading algorythm------------------------------------------
this portion of code is what opens books by asking user for input for Book (book_abrev) and Book Verse (verse) and displays scriptuer by verse
"""

#flag to exit program
done = False

def main(booktype):
    global done
    #check exit flag
    if done == True:
        exit()
    else:
#print Titles
#        if booktype == "./KJVA":
#            titles.kjv()
#        elif booktype == "./RSV":
#            titles.rsv()                                                                                  #disply options

# Enter Book Title/abbreciation
        print("-----"*10 , "Welcome" , "-----"*10)
        book_abrev = input("Please Enter book Name: ") 
        book_name = abbreviation.shorthand(book_abrev.lower())

        if book_name == 'q':
            done = True
            main(booktype)
        else:
            verse_inpt = input("Please Enter Verse Number: ")

            if verse_inpt == 'q':
                done = True
                main(booktype)

#enter Values and get outputs
            else:
                bible_ver = Book(book_name, verse_inpt, "", "", "", "")
                book_txt = bible_ver.format_bk()                                                      #add .txt to end of file
                bible_str = bible_ver.open_bk(book_txt, booktype)                                           #open file in string
                ver_index = bible_ver.create_vrs_idex()                                              #crate verse index
                verse_index = bible_ver.index_vrs(bible_str, ver_index[0], ver_index[1])              #index verse
                bible_ver.print_verse(bible_str, verse_index[0], verse_index[1], booktype)                #display verse


class Book:
        """
        -------------------------------------------------------Book Class
        This class contains functaions that sort through scripture for the specific vers that is being searched
        
        Example:
            Book.print_verse(bible_str, verse_index[0], verse_index[1])
        """

        def __init__(self, book, verse, year, author, version, bookloc):
            self.book = book
            self.year = year
            self.author = author
            self.verse = verse
            self.bookloc = bookloc
        
        def format_bk(self):
            """
            This takes the txt fromat for book and adds .txt to pull document
            """
            book = self.book+'.txt'
            return book

        def open_bk(self, book, booktype):
            """
            This function opens a specific book and attempts to return it as a string
            """
            span_bible = open(book,"r")
            span_bible = codecs.open(book,"r", encoding = 'utf8') 
            span_bible_book= span_bible.read()

            try:
               span_bible = open(book,"r")
               span_bible_book= span_bible.read()
            except Exception:
                input("Book not found press ENTER!")
                main(booktype)
            return span_bible_book

        def create_vrs_idex(self):
            """
            This Function checks if verse exists and creates index to allow for calling of specific verses
            """
            try:
                next_verse = int(self.verse) + 1                     #find start of next verse
                verse_str = str(self.verse+":")                      #create verse serch index
                next_verse_str = str(str(next_verse) + ":")     #create verse search index of nex verse
            except Exception:
                verse = "999999"
            return verse_str, next_verse_str                    #return search indexes

        def index_vrs(self, span_bible_book, verse_str, next_verse_str):
            """
            generate index start and index end
            """
            bible_string_len = len(span_bible_book)

            #get verse beginning
            try:
                verse_start=span_bible_book.index(verse_str)
            except Exception:
                verse_start=0
            #get verse end
            try:
                verse_end=span_bible_book.index(next_verse_str)
            except Exception:
                verse_end=bible_string_len    
            return verse_start, verse_end

        def print_verse(self, span_bible_book, verse_start, verse_end, booktype):
            """
            Print Final Results
            """
            # os.system('cls')
            print(span_bible_book[verse_start:verse_end])
            answer = input("press any key to continue: or q to quit")

            if answer == 'q':
                global done
                done = True
                main(booktype)
            else:
                main(booktype)

"""
----------------------------------------------------------------------Select Version---------------------------------------------------------------
this section assign oustide variables of book
"""

version = input("Select Version \n 1 = KJV \n 2 = RSV \n")

if version == "1":
    bible_ver = Book("", "", 1909, "Cipriano de Valera", "Reina-Valera", "./KJVA")
elif version == "2":
    bible_ver = Book("", "", 0000, "God", "KJV", "./RSV")

#Change Directroy to location of specified bible
dir_loc = bible_ver.bookloc
os.chdir(dir_loc)

#start main Functon
main(bible_ver.bookloc)
