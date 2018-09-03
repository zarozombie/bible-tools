import os
import re
import sys
import argparse

#display books
print("1 Genesis\n"+
"2 Exodus\n"+
"3 Leviticus\n"+
"4 Numbers\n"+
"5 Deuteronomy\n"+
"6 Joshua\n"+
"7 Judges\n"+
"8 Ruth\n"+
"9 1 Samuel\n"+
"10 2 Samuel\n"+
"11 1 Kings\n"+
"12 2 Kings\n"+
"13 1 Chronicles\n"+
"14 2 Chronicles\n"+
"15 Ezra\n"+
"16 Nehemiah\n"+
"17 Esther\n"+
"18 Job\n"+
"19 Psalms\n"+
"20 Proverbs\n"+
"21 Ecclesiastes\n"+
"22 Song of Solomon\n"+
"23 Isaiah\n"+
"24 Jeremiah\n"+
"25 Lamentations\n"+
"26 Ezekiel\n"+
"27 Daniel\n"+
"28 Hosea\n"+
"29 Joel\n"+
"30 Amos\n"+
"31 Obadiah\n"+
"32 Jonah\n"+
"33 Micah\n"+
"34 Nahum\n"+
"35 Habakkuk\n"+
"36 Zephaniah\n"+
"37 Haggai\n"+
"38 Zechariah\n"+
"39 Malachi\n"+
"40 Matthew\n"+
"41 Mark\n"+
"42 Luke\n"+
"43 John\n"+
"44 Acts\n"+
"45 Romans\n"+
"46 1 Corinthians\n"+
"47 2 Corinthians\n"+
"48 Galatians\n"+
"49 Ephesians\n"+
"50 Philippians\n"+
"51 Colossians\n"+
"52 1 Thessalonians\n"+
"53 2 Thessalonians\n"+
"54 1 Timothy\n"+
"55 2 Timothy\n"+
"56 Titus\n"+
"57 Philemon\n"+
"58 Hebrews\n"+
"59 James\n"+
"60 1 Peter\n"+
"61 2 Peter\n"+
"62 1 John\n"+
"63 2 John\n"+
"64 3 John\n"+
"65 Jude\n"+
"66 Revelation")


book = input("select your book:")
book = book+'.txt'

span_bible = open(book,"r")
span_bible_book= span_bible.read()

os.system('cls')

verse = input("select verse:")

os.system('cls')

next_verse = int(verse) + 1
verse_str = str(verse+":")

next_verse_str = str(str(next_verse) + ":")

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
# print(bible_string_len)
# acdc = 0
# re.match('1:',span_bible_book)
# for x in range(0, bible_string_len):
#     try:
#         acdc = span_bible_book.index("1:",acdc)
#         print(acdc)
#         acdc = acdc+1
#     except Exception:
#         acdc = acdc+1
#     continue

# print(span_bible_book[11:58349])

# abc = span_bible_book_list[1].index("1:")
# print(abc)
# if '1:' in span_bible_book_list :
    # print("Yes, 'at' found in List : " , listOfStrings)

# 1 Genesis
# 2 Exodus
# 3 Leviticus
# 4 Numbers
# 5 Deuteronomy
# 6 Joshua
# 7 Judges
# 8 Ruth
# 9 1 Samuel
# 10 2 Samuel
# 11 1 Kings
# 12 2 Kings
# 13 1 Chronicles
# 14 2 Chronicles
# 15 Ezra
# 16 Nehemiah
# 17 Esther
# 18 Job
# 19 Psalms
# 20 Proverbs
# 21 Ecclesiastes
# 22 Song of Solomon
# 23 Isaiah
# 24 Jeremiah
# 25 Lamentations
# 26 Ezekiel
# 27 Daniel
# 28 Hosea
# 29 Joel
# 30 Amos
# 31 Obadiah
# 32 Jonah
# 33 Micah
# 34 Nahum
# 35 Habakkuk
# 36 Zephaniah
# 37 Haggai
# 38 Zechariah
# 39 Malachi
# 40 Matthew
# 41 Mark
# 42 Luke
# 43 John
# 44 Acts
# 45 Romans
# 46 1 Corinthians
# 47 2 Corinthians
# 48 Galatians
# 49 Ephesians
# 50 Philippians
# 51 Colossians
# 52 1 Thessalonians
# 53 2 Thessalonians
# 54 1 Timothy
# 55 2 Timothy
# 56 Titus
# 57 Philemon
# 58 Hebrews
# 59 James
# 60 1 Peter
# 61 2 Peter
# 62 1 John
# 63 2 John
# 64 3 John
# 65 Jude
# 66 Revelation

# Genesis.txt
# Exodus.txt
# Leviticus.txt
# Numbers.txt
# Deuteronomy.txt
# Joshua.txt
# Judges.txt
# Ruth.txt
# 1 Samuel.txt
# 2 Samuel.txt
# 1 Kings.txt
# 2 Kings.txt
# 1 Chronicles.txt
# 2 Chronicles.txt
# Ezra.txt
# Nehemiah.txt
# Esther.txt
# Job.txt
# Psalms.txt
# Proverbs.txt
# Ecclesiastes.txt
# Song of Solomon.txt
# Isaiah.txt
# Jeremiah.txt
# Lamentations.txt
# Ezekiel.txt
# Daniel.txt
# Hosea.txt
# Joel.txt
# Amos.txt
# Obadiah.txt
# Jonah.txt
# Micah.txt
# Nahum.txt
# Habakkuk.txt
# Zephaniah.txt
# Haggai.txt
# Zechariah.txt
# Malachi.txt
# Matthew.txt
# Mark.txt
# Luke.txt
# John.txt
# Acts.txt
# Romans.txt
# 1 Corinthians.txt
# 2 Corinthians.txt
# Galatians.txt
# Ephesians.txt
# Philippians.txt
# Colossians.txt
# 1 Thessalonians.txt
# 2 Thessalonians.txt
# 1 Timothy.txt
# 2 Timothy.txt
# Titus.txt
# Philemon.txt
# Hebrews.txt
# James.txt
# 1 Peter.txt
# 2 Peter.txt
# 1 John.txt
# 2 John.txt
# 3 John.txt
# Jude.txt
# Revelation.txt