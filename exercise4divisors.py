import sys
import random

###########################################################
#http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
number=int(input("Enter a number:>>\n"))
d=[]

for i in range(1,number+1):
	if number%i==0:
		d+=[i]
print('All divisors of {} are: {}'.format(number, d))


###########################################################
print('This program has finished. \n Press Enter to exit')
input()
sys.exit()