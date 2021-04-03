import string
from random import choice

ln = int(input("Length: "))
alpha = input("Alpha:")
alpha = True if alpha.lower() == 'y' else False
characters = string.digits
if alpha:
    characters += string.ascii_letters
password =  "".join(choice(characters) for x in range(ln))
print (password)
