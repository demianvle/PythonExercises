import sys
import random
import codecs
###########################################################
number=int(input("Enter a number\n"))
check=int(input("enter a number to divide by\n"))
print("\n")
if number%4==0:
	print("%d is a multiple of 4"% number)
elif number%2==0:
	print("The number you entered is an even integer")
else:
	print("The number you entered is an odd integer")
print("\n")
if number%check==0:
	print("The number: {} you entered is evenly divisible by {}".format(number, check))
else:
	print("The number: {} you entered not evenly divisible by {}".format(number, check))
###########################################################
print('This program has finished. \n Press Enter to exit')
#input()
sys.exit()