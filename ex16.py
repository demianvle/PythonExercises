import sys
import random
import timeit
##################################################
""" Password Generator
Exercise 16 (and Solution)

Write a password generator in Python. Be creative with how you generate passwords - 
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.

Extra:

    Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""
def passgen(strength):
    if strength==1:
        randompass=""
        randompassnums= random.randint(10,99)
        randompassletters="abcdefghijklmnopqrstuvwxyz!@#$%^&*ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"
        for i in range(0, 6):
            randompass+=randompassletters[random.randint(0,len(randompassletters)-1)]
        randompass=randompass+str(randompassnums)
        print(randompass)

    elif strength ==2:
        randompass=""
        randompassnums= random.randint(10,99)
        randompassletters="There is always time for the heart of the weak to grow strong And the soul of the strong can always fall into darkness".split()
        for i in range(0, 2):
            randompass+=randompassletters[random.randint(0,len(randompassletters)-1)]
        randompass+= str(randompassnums)
        print(randompass)
    else:
        print("Enter 1 or 2. Try again...")
        passgen_with_options()


def passgen_with_options():
    strength=input("Type '1' for a strong password. Type '2' for a weak password.\n...")
    print("Your new random password is:\n")
    passgen(int(strength))



passgen_with_options()

#############################################
print("\n The execution time was: {}".format(timeit.timeit(number = 10000)))
#############################################
sys.exit()

