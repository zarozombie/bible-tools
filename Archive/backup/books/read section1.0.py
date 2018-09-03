import os
import re
import sys
import argparse

#display books
def title():
    print("Genesis\n"+
    "Exodus\n"+
    "Leviticus\n"+
    "Numbers\n"+
    "Deuteronomy\n"+
    "Joshua\n"+
    "Judges\n"+
    "Ruth\n"+
    "1 Samuel\n"+
    "2 Samuel\n"+
    "1 Kings\n"+
    "2 Kings\n"+
    "1 Chronicles\n"+
    "2 Chronicles\n"+
    "Ezra\n"+
    "Nehemiah\n"+
    "Esther\n"+
    "Job\n"+
    "Psalms\n"+
    "Proverbs\n"+
    "Ecclesiastes\n"+
    "Song of Solomon\n"+
    "Isaiah\n"+
    "Jeremiah\n"+
    "Lamentations\n"+
    "Ezekiel\n"+
    "Daniel\n"+
    "Hosea\n"+
    "Joel\n"+
    "Amos\n"+
    "Obadiah\n"+
    "Jonah\n"+
    "Micah\n"+
    "Nahum\n"+
    "Habakkuk\n"+
    "Zephaniah\n"+
    "Haggai\n"+
    "Zechariah\n"+
    "Malachi\n"+
    "Matthew\n"+
    "Mark\n"+
    "Luke\n"+
    "John\n"+
    "Acts\n"+
    "Romans\n"+
    "1 Corinthians\n"+
    "2 Corinthians\n"+
    "Galatians\n"+
    "Ephesians\n"+
    "Philippians\n"+
    "Colossians\n"+
    "1 Thessalonians\n"+
    "2 Thessalonians\n"+
    "1 Timothy\n"+
    "2 Timothy\n"+
    "Titus\n"+
    "Philemon\n"+
    "Hebrews\n"+
    "James\n"+
    "1 Peter\n"+
    "2 Peter\n"+
    "1 John\n"+
    "2 John\n"+
    "3 John\n"+
    "Jude\n"+
    "Revelation\n"+
    "--------------------\n"+
    "q to Quit\n")

def main():
    os.system('cls')
    title()
    book = input("select your book:")
    book = book+'.txt'

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

    verse = input("a to display all \n\n-------------------------- \n\nselect verse:")

    os.system('cls')

    try:
        next_verse = int(verse) + 1
        verse_str = str(verse+":")
        next_verse_str = str(str(next_verse) + ":")
    except Exception:
        # if verse =="a":
        #     verse_start=0
        verse = "999999"

    bible_string_len = len(span_bible_book)
    # bible_string_len = int(bible_string_len)

    try:
        verse_start=span_bible_book.index(verse_str)
    except Exception:
        verse_start=0

    try:
        verse_end=span_bible_book.index(next_verse_str)
    except Exception:
        verse_end=bible_string_len    



    # print(verse_start)
    # print(verse_end)
    print(span_bible_book[verse_start:verse_end])

    span_bible_book_list = span_bible_book.split('\n')

    bible_string_len = len(span_bible_book)
    bible_string_len = int(bible_string_len)

    input("press any key to continue:")
    main()

main()