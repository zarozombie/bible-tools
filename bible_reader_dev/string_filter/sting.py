import re
bible_string = input("enter bible string: ")
parse_string = []

#regular expresion used to parse data
parse_string = re.split(' |:|-', bible_string)

print(parse_string)

