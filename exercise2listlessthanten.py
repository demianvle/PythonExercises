import sys
import random

###########################################################
#http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for num in a:
	if num<5:
		print(num)

#Extra 1
b=[]
for num in a:
	if num<5:	
		b+=[num]
print(b)
#Extra 3
b=[]
number=int(input('Enter a number:\n'))
for num in a:
	if num<number:	
		b+=[num]
print(b)

###########################################################
print('This program has finished. \n Press Enter to exit')
input()
sys.exit()