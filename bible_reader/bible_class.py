import codecs
import main

# =============== Old Dependancies / Modules / Libraries. Maybe remove them next revision
#import titles
#import abbreviation
#import logging

class Book:
        """
        -------------------------------------------------------Book Class
        This class contains functaions that sort through scripture for the specific vers that is being searched
        
        Example:
            Book.print_verse(bible_str, verse_index[0], verse_index[1])
        """

        def __init__(self, book, verse, year, author, version, bookloc):
            self.book = book
            self.verse = verse
            self.year = year
            self.author = author
            self.version = version
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
#            open_bible = open(book,"r")
#            open_bible = codecs.open(book,"r", encoding = 'utf8') 
#            read_bible= open_bible.read()

            try:
               open_bible = open(book,"r")
               read_bible = open_bible.read()
            except Exception:
                input("Book not found press ENTER!")
                main.main(booktype)
            return read_bible

        def create_vrs_idex(self):
            """
            This Function formats verse string and next verse string (i.e if input + "22" | verse_str will equal 22: | next_verse_str will equal 23: )
            """
            next_verse = int(self.verse) + 1                     #find start of next verse
            verse_str = str(self.verse + ":")                      #create verse serch index
            next_verse_str = str(str(next_verse) + ":")     #create verse search index of nex verse
            
            #########################need to create way to have verse input with x:x be used (i.e 32:11) also support for Book X:X (i.e gen 32:11)
                #next_verse_str = str(str(next_verse))     #create verse search index of nex verse
            

            return verse_str, next_verse_str                    #return search indexes

        def index_vrs(self, bible_book, verse_str, next_verse_str):
            """
            generate index start and index end for verse str
            """
            bible_string_len = len(bible_book)

            #get verse beginning
            try:
                verse_start = bible_book.index(verse_str)
            except Exception:
                verse_start = 0
            #get verse end
            try:
                verse_end = bible_book.index(next_verse_str)
            except Exception:
                verse_end = bible_string_len    
            return verse_start, verse_end

        def print_verse(self, span_bible_book, verse_start, verse_end, booktype):
            """
            Print Final Results
            """
            print(span_bible_book[verse_start:verse_end])
            answer = input("press any key to continue: or q to quit")

            if answer == 'q':
                quit()
            else:
                main.main(booktype)
