import titles
import os

#flag to exit program
done = False

def main():
    global done
    #check exit flag
    if done == True:
        exit()
    else:
        titles.title()                                                                                #disply options
        book_name = input("Please Enter book Name:")                                                  #user types book name
        #see if user wants to exit program        
        if book_name == 'q':
            done = True
            main()
        else:
            verse = input("Please Enter Verse Number:")
            #see if user wants to exit program
            if verse == 'q':
                done = True
                main()
            else:
                #create opjects
                Holy_book = Book("holy Bible", 1, 0000, "God", "KJV")
                Reina_Valera = Book(book_name, verse, 1909, "Cipriano de Valera", "Reina-Valera")
                
                book = Reina_Valera.format_book()                                                      #add .txt to end of file
                spanish_bible = Reina_Valera.open_book(book)                                           #open file in string
                index = Reina_Valera.create_verse_index()                                              #crate verse index
                verse_index = Reina_Valera.index_verse(spanish_bible, index[0], index[1])              #index verse
                Reina_Valera.print_verse(spanish_bible, verse_index[0], verse_index[1])                #display verse

class Book:
        def __init__(self, book, verse, year, author, version):
            self.book = book
            self.year = year
            self.author = author
            self.verse = verse
        
        def format_book(self):
            book = self.book+'.txt'
            return book

        def header(self):
            return "hello World"
            # print(self.book)

        def open_book(self, book):
            #open specific bible book if book does not exist loops main
            try:
                span_bible = open(book,"r")
                span_bible_book= span_bible.read()
            except Exception:
                input("Book not found press ENTER!")
                main()
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

        def print_verse(self, span_bible_book, verse_start, verse_end):
            # os.system('cls')
            print(span_bible_book[verse_start:verse_end])

            #end of statement
            answer = input("press any key to continue: or q to quit")
            if answer == 'q':
                global done
                done = True
                main()
            else:
                main()
main()