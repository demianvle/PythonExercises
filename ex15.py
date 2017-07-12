import sys
import random
##################################################

""" Reverse Word Order
Exercise 15 (and Solution)
Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order."""
def reverse(words):
    words = words.split()
    print(words)
    words=" ".join(words[::-1])
    print(words)

reverse("This is a stupid quote")




#############################################
sys.exit()

