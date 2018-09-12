import titles
import os
import abbreviation
import logging
import codecs


"""
------------------------------------------------------------------Book Reading algorythm------------------------------------------
this portion of code is what opens books and displays scriptuer by verse
"""

#flag to exit program
done = False

def main(book_type):
    global done
    #check exit flag
    if done == True:
        exit()
    else:
        # # titles.kjv()
        # print(book_type)
        if book_type == "./KJVA":
            titles.kjv()
        elif book_type == "./RSV":
            titles.rsv()                                                                                  #disply options
        # book_name = input("Please Enter book Name:")  
        book_abrev = input("Please Enter book Name:")  
        #user types book name
        book_name = abbreviation.shorthand(book_abrev)
        #see if user wants to exit program        
        if book_name == 'q':
            done = True
            main(book_type)
        else:
            verse = input("Please Enter Verse Number:")
            #see if user wants to exit program
            if verse == 'q':
                done = True
                main(book_type)
            else:
                #create opjects
                # logging.basicConfig(filename='test.log', level=logging.DEBUG,
                # format='%(asctime)s:%(levelname)s:%(message)s')
                # logging.debug(book_name, verse)

                Reina_Valera = Book(book_name, verse, "", "", "", "")
                book = Reina_Valera.format_book()                                                      #add .txt to end of file
                spanish_bible = Reina_Valera.open_book(book, book_type)                                           #open file in string
                index = Reina_Valera.create_verse_index()                                              #crate verse index
                verse_index = Reina_Valera.index_verse(spanish_bible, index[0], index[1])              #index verse
                Reina_Valera.print_verse(spanish_bible, verse_index[0], verse_index[1], book_type)                #display verse


"""
-------------------------------------------------------Book Class

This class contains functaions that sort through scripture for the specific vers that is being searched

Example:
    Book.print_verse(spanish_bible, verse_index[0], verse_index[1])

    
"""
class Book:
        def __init__(self, book, verse, year, author, version, bookloc):
            self.book = book
            self.year = year
            self.author = author
            self.verse = verse
            self.bookloc = bookloc
        
        def format_book(self):
            book = self.book+'.txt'
            return book

        def header(self):
            return "hello World"
            # print(self.book)

        def open_book(self, book, book_type):
            #open specific bible book if book does not exist loops main

            #testing notes
            book = "Genesis.txt"
            #span_bible = open(book,"r")
            #span_bible = codecs.open(book,"r", encoding = 'utf8') 
            # span_bible_book= span_bible.read()
            try:
                span_bible = open(book,"r")
                span_bible_book= span_bible.read()
            except Exception:
                input("Book not found press ENTER!")
                main(book_type)
            # os.system('cls')
            return span_bible_book

        def create_verse_index(self):
            # os.system('cls')
            #check if verse exists
            try:
                next_verse = int(self.verse) + 1                     #find start of next verse
                verse_str = str(self.verse+":")                      #create verse serch index
                next_verse_str = str(str(next_verse) + ":")     #create verse search index of nex verse
            except Exception:
                verse = "999999"
            return verse_str, next_verse_str                    #return search indexes

        def index_verse(self, span_bible_book, verse_str, next_verse_str):
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

        def print_verse(self, span_bible_book, verse_start, verse_end, book_type):
            # os.system('cls')
            print(span_bible_book[verse_start:verse_end])

            #end of statement
            answer = input("press any key to continue: or q to quit")
            if answer == 'q':
                global done
                done = True
                main(book_type)
            else:
                main(book_type)


"""
----------------------------------------------------------------------Select Version---------------------------------------------------------------
this section assign oustide variables of book
"""
# print("select version")
version = input("Select Version \n 1 = KJV \n 2 = RSV \n")

if version == "1":
    # print("KJV")
    # input("press Enter")
    Reina_Valera = Book("", "", 1909, "Cipriano de Valera", "Reina-Valera", "./KJVA")
elif version == "2":
    # print("RSV")
    # input("Press Enter")
    Reina_Valera = Book("", "", 0000, "God", "KJV", "./RSV")



# original instance assignments
# Holy_book = Book("holy Bible", 1, 0000, "God", "KJV", "./b")
# Reina_Valera = Book("", "", 1909, "Cipriano de Valera", "Reina-Valera", "./b")

# instance assignmet with variable names for arguments
# Reina_Valera = Book(bookver, vernum, datepub, bibauth, bibtitle, biblocation)


dir_loc = Reina_Valera.bookloc
# os.chdir(Reina_Valera.bookloc)
os.chdir(dir_loc)
main(Reina_Valera.bookloc)