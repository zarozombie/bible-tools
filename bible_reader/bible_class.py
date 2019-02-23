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
                main.main(booktype)
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
            print(span_bible_book[verse_start:verse_end])
            answer = input("press any key to continue: or q to quit")

            if answer == 'q':
                quit()
            else:
                main.main(booktype)
