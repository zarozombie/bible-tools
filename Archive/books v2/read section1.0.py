import os
import re
import sys
import argparse
import titles

class Bible:
    def __init__(self, book, verse):
        self.book = book
        self.verse = verse

    def main(self):
        os.system('cls')
        titles.title()

        book = book+'.txt'
        return book

    def open_book(self):
        #open specific bible book if book does not exist loops main
        try:
            span_bible = open(book,"r")
            span_bible_book= span_bible.read()
        except Exception:
            if book == 'q.txt':
                quit()
            else:
                main()
        os.system('cls')
        return span_bible_book

    def choose_verse(self):
        #select specific bible verse

        os.system('cls')
        #check if verse exists
        try:
            next_verse = int(verse) + 1                     #find start of next verse
            verse_str = str(verse+":")                      #create verse serch index
            next_verse_str = str(str(next_verse) + ":")     #create verse search index of nex verse
        except Exception:
            verse = "999999"
        return verse_str, next_verse_str                    #return search indexes

    def index_verse(self, verse_str, next_verse_str):
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

    def print_verse(self, verse_start, verse_end):
        #print Verse 
        # print(verse_start)
        # print(verse_end)
        print(span_bible_book[verse_start:verse_end])

        #end of statement
        input("press any key to continue:")
        main()
    book = input("select a book:")
    verse = input("a to display all \n\n-------------------------- \n\nselect verse:")
    spanish_bible = Bible(book, verse)
    # span_bible_book = open_book()
    # selected_verse = choose_verse()
    # verse_index = index_verse(selected_verse[0],selected_verse[1])
    # print_verse(verse_index[0], verse_index[1])








def main():
    os.system('cls')
    titles.title()
    book = input("select a book:")
    book = book+'.txt'
    return book

def open_book():
    #open specific bible book if book does not exist loops main
    try:
        span_bible = open(book,"r")
        span_bible_book= span_bible.read()
    except Exception:
        if book == 'q.txt':
            quit()
        else:
            main()
    os.system('cls')
    return span_bible_book

def choose_verse():
    #select specific bible verse
    verse = input("a to display all \n\n-------------------------- \n\nselect verse:")
    os.system('cls')
    #check if verse exists
    try:
        next_verse = int(verse) + 1                     #find start of next verse
        verse_str = str(verse+":")                      #create verse serch index
        next_verse_str = str(str(next_verse) + ":")     #create verse search index of nex verse
    except Exception:
        verse = "999999"
    return verse_str, next_verse_str                    #return search indexes

def index_verse(verse_str, next_verse_str):
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

def print_verse(verse_start, verse_end):
    #print Verse 
    # print(verse_start)
    # print(verse_end)
    print(span_bible_book[verse_start:verse_end])

    #end of statement
    input("press any key to continue:")
    main()

# book = main()
# span_bible_book = open_book()
# selected_verse = choose_verse()
# verse_index = index_verse(selected_verse[0],selected_verse[1])
# print_verse(verse_index[0], verse_index[1])

#using list instead of string
# span_bible_book_list = span_bible_book.split('\n')

# bible_string_len = len(span_bible_book)
# bible_string_len = int(bible_string_len)
# print ("this is the test results")
# print (test[0])
