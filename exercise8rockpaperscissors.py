import sys


###########################################################
#http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner, and ask if the
players want to start a new game)
Remember the rules:
    Rock beats scissors
    Scissors beats paper
    Paper beats rock'''
print('Enter 1 for new game and 2 to exit.\n')
instruction=''
def instruct():
	instruction=int(input('1 for new, 2 to exit'))

while instruction != 2:
	print('Remember the rules: Rock beats scissors.Scissors beats paper. Paper beats rock')
	print('Make a choice, you know the game:\n')
	p1=input('paper, rock or scissors')
	p2= input('paper, rock or scissors')
	if p1==p2:
		print('Try again, no one wins this round.')
	elif p1=='paper'and p2=='rock' or p1=='scissors' and p2=='paper' or p1=='rock' and p2=='scissors':
		print('player 1 wins this round')
	else:
		print('player 2 wins this round')
	instruct()


###########################################################
print('This program has finished. \n Press Enter to exit')
input()
sys.exit()