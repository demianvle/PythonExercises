import sys
import random

###########################################################
#http://www.practicepython.org/exercise/2014/02/26/04-divisors.html

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in a and b:
	if i in a and i in b and i not in c:
		c+=[i]
print(c)

#extra 1. Randomly generate two lists to test this
d=[]
e=[]
f=[]
for i in range(0, 100):
	d+=[i+random.randint(0,10)]
	e+=[i+random.randint(0,10)]
print(d,e)

#compare lists
for i in d and e:
	if i in d and i in e and i not in f:
		f+=[i]
print(f)



###########################################################
print('This program has finished. \n Press Enter to exit')
input()
sys.exit()