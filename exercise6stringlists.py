import sys
import random

###########################################################
#http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
word= input('Enter a word to check if its a palindrome:\n')
print(word)
newword=''

for letter in range(1,len(word)+1):
	newword+=word[-letter]

print(newword)

if newword==word:
	print('The word is palindrome indeed.')
else:
	print('not a palindrome, try again later.')
#The following solution was offered by:
#https://gist.github.com/anonymous/3299da3707670a919d4d
#I had not seen this: name[::-1]
"""Ask the user for a string and print out whether this string is a palindrome or not.
 (A palindrome is a string that reads the same forwards and backwards.)"""

name = input("Enter a string ")
name_reversed = name[::-1]

if name == name_reversed:
    print("A palindrome string")
else:
	print("Not a palindrom string")

###########################################################
print('This program has finished. \n Press Enter to exit')
input()
sys.exit()