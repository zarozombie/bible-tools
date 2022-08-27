import codecs

"""
This is to Describe the Module
"""
# =============== Old Dependancies / Modules / Libraries. Maybe remove them next revision
#import titles
#import abbreviation
#import logging


class Book:
    """
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

    def add_txt(self):
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
            open_bible = open(book, "r")
            read_bible = open_bible.read()
        except Exception:
            input("Book not found press ENTER!\n")
            main.main(booktype)
        return read_bible

    def create_vrs_idex(self):
        """
        This Function formats verse string and next verse string (i.e if input + "22" | verse_str will equal 22: | next_verse_str will equal 23: )
        """
        next_verse = int(self.verse) + 1  # find start of next verse
        verse_str = str("{" + self.verse + ":")  # create verse serch index
        # create verse search index of nex verse
        next_verse_str = str("{" + str(next_verse) + ":")

        # need to create way to have verse input with x:x be used (i.e 32:11) also support for Book X:X (i.e gen 32:11)
        # next_verse_str = str(str(next_verse))     #create verse search index of nex verse

        return verse_str, next_verse_str  # return search indexes

    def index_vrs(self, bible_book, verse_str, next_verse_str):
        """
        generate index start and index end for verse str
        """
        bible_string_len = len(bible_book)

        # get verse beginning
        try:
            verse_title = bible_book.split('\n')
        except Exception:
            print("did not work")
        try:
            verse_start = bible_book.index(verse_str)
        except Exception:
            verse_start = 0
        # get verse end
        try:
            verse_end = bible_book.index(next_verse_str)
        except Exception:
            verse_end = bible_string_len
        return verse_start, verse_end, verse_title

    def print_verse(self, bible_str, verse_start, verse_end, booktype):
        print(bible_str[verse_start:verse_end])
        answer = input(
            "\n\n-----------------------\n\npress any key to continue: or q to quit\n")

        if answer == 'q':
            quit()
        else:
            main.main(booktype)
