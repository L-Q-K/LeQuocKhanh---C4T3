from time import *

s = input("Some string: ")
letters_count = {}

for letter in s:
    letter = letter.lower()
    if letter not in "~,!@#$%^&*()_+|`-=\?/><.,\";:]{][ ":
        letters_count[letter] = letters_count.get(letter, 0) + 1

letters_count = list(letters_count.items())
letters_count.sort()
print(*letters_count, sep='\n')

sleep(3)
