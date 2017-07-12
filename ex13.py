import sys
##################################################
#  I did not solve this one by myself. I watched a video and copied the solution while trying to understand it.
#http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
"""Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum 
of the previous two numbers in the sequence.
 The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)"""
n= int(input("Enter the amount of numbers to generate for the fibonnaci sequence.\n>>>"))
a=0
b=1
if n<=0:
    print("Ok, so you don't wanna play. We are ending this now.\n")
    sys.exit()
elif n== 1:
    print(a)
elif n >= 2:
    print("{}, {} ".format(a,b,),end='')
    for i in range(2,n):
        c=a+b
        print(", {}".format(c),end='')
        a=b
        b=c



#################################################3
sys.exit()

