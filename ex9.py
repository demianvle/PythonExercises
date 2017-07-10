import sys
import random
############################################

def game():
    guesses=1 # Sets the guess counter.
    randnum = random.randint(1, 10) # Generates the random number.
    num = input('What number am I thinking? Guess\n') # Requests for input.
    try: #Try will make sure the input is an int. If not, will give the option to leave or restart.
        if int(num):
            while num is not randnum:
                if int(num) < randnum:
                    print("Too low. Try a higher number.")
                    num = input('Try again\n') #New attempt.
                    guesses += 1  #Increases the guess counter.
                    print("guess counter " + str(guesses))
                elif int(num) > randnum:
                    print("Too high. Try a lower number.")
                    num = input('Try again\n')
                    guesses += 1
                    print("guess counter " + str(guesses))
                else: #Will inform the number has been guessed and will offer a new attempt.
                    print("You got it. It took you {} attempts.".format(guesses))
                    newgame = input("Do you want to continue? If you do, enter 'y', otherwise enter'exit'\n")
                    while newgame is not "y" and newgame is not "exit":
                        if newgame == "y":
                            print("Ok, lets play again.")
                        elif newgame == "exit":
                            print("Game over")
                            break
                        elif newgame is not "y" or newgame is not "exit":
                            print("y or exit")
                            newgame = input("Do you want to continue? If you do, enter 'y', otherwise enter'exit'\n")
                    else:
                        game()
    except ValueError:
        if num == "exit":
            print("Good bye")
            sys.exit()
        else:
            print("Must use an Integer.\n"
                "If you would like to exit, type exit.\n"
                "Let us star all over again.\n")
            game()


game()






############################################

sys.exit()
