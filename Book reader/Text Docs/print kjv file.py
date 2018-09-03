import os

try:
	os.chdir('./Text Docs') 
except Exception:
	print(os.getcwd())
	# input("")

def open_book():
	try:
		# span_bible = open("kjv.txt" , "r")
		# span_bible = open("rsv.txt" , "r")
		span_bible = open("weblinks.1.5.txt", "r")
		span_bible = span_bible.read()
	except Exception:
		input("Book not found press ENTER!")
	# os.system('cls')
	# return span_bible_book
	# span_bible_book= span_bible.read()
	# # a = span_bible.split('\n')
	# b = span_bible.split('\n')
	# a = b.split('.txt')
	# print(span_bible)
	a = span_bible.split('\n')
	# a = span_bible.split('.txt\n')
	rangez = len(a)-1
	# print(len(a)-1)
	for x in range(rangez):
		print(a[x])
		# print("\"" + a[x] + "\\n" + "\"")

a = open_book()