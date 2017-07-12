import sys
import random
##################################################
#http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
"""Exercise 14 (and Solution)

Write a program (function!) that takes a list and returns a new list that contains
 all the elements of the first list minus all the duplicates.

Extras: Write two different functions to do this - one using a loop and constructing a list, and another using sets.
"""
#setex=set() setex.add() setex.remove() setex.discard()
#Option 1, using lists.
def list1(a,b):
    randomlist=[]
    newlist=[]
    #builds the randomlist
    for i in range(0,a):
        num = random.randint(0,b)
        randomlist+=[num]
    print(randomlist)
    #removes the duplicated elements
    for i in randomlist:
        if i not in newlist:
            newlist+=[i]
    return newlist


print(list1(100,20))

#Option 2, using sets.

def list2(a,b):
    randomlist=set()
    for i in range(0, a):
        randomlist.add(random.randint(0, b))
    return randomlist

print(list2(100,20))
#############################################
sys.exit()

