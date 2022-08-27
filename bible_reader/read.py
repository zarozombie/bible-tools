import os
import bible_class
import main

bible_version = input("\nSelect Version \n 1 = KJV \n 2 = RSV \n")

if bible_version == "1":
    bible_ver = bible_class.Book(
        "", "", 1909, "Cipriano de Valera", "Reina-Valera", "./KJVA")
elif bible_version == "2":
    bible_ver = bible_class.Book("", "", 0000, "God", "KJV", "./RSV")
elif bible_version == "q":
    quit()

dir_loc = bible_ver.bookloc
os.chdir(dir_loc)

main.main(bible_ver.bookloc, bible_ver)
