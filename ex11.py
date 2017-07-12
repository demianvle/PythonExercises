import sys
##################################################

#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def primes():
    num = int(input("Enter a number to confirm if it is a prime number.\n>>"))
    for i in range(2, num):
        if num % i is 0:
            print("This is not prime number.")
            break
        elif i == num-1:
            print("This is a prime number.")



primes()

#################################################3
sys.exit()

