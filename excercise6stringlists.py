import sys
import random

###########################################################
#http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
word= input('Enter a word to check if its a palindrome:\n')
print(word)
for letter in range(0, len(word),-1):
	new+=letter
	print(new)
print(word)
###########################################################
print('This program has finished. \n Press Enter to exit')
input()
sys.exit()