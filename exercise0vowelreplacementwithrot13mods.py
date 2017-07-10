import sys
import random
import codecs
###########################################################
vowels=('a','e','i','o','u')
message=str(input('Enter your message: '))
new_message=''
for letter in message:
	if letter not in vowels:
		print(letter+" not a vowel")
		encletter=codecs.encode(letter, "rot13")
		new_message+=encletter
	else:
		print(letter+' vowel')
		randomletter=random.randint(0,4)
		new_message+=vowels[randomletter]
print(new_message)

###########################################################
print('This program has finished. \n Press Enter to exit')
#input()
sys.exit()