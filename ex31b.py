# Squares memorization drill game
# Asks the player to guess the square of a number from 1 to 16
# Players get 10 questions and get their score out of 10 at the end

from random import randint
import os

def header():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("* " * 5 + "Welcome to Guess the Square!" + "* " * 5)


header()

again = "y"
while again != "n":
	# reset variables before starting the for loop
	correct = 0	# keeps track of correct answers		
	root = 0	# setting the initial vlue of root to 0. I need this in the while loop inside the for loop...
	drawn_nums = [0]	# keeps track of the numbers already drawn from randint(1, 16). Initializing with 0
	
	for i in range(1,11):
		while root in drawn_nums:	# on the first iteration root is in drawn_nums becasue I set it to 0 up there
			root = randint(1,16)	
		drawn_nums.append(root)		# add the number we just got from randint() to drawn_nums. This prevents repeats.

		# evaluate the input
		guess = int(input(f"What is the square of {root}? "))
		if guess == (root ** 2):
			print("Correct!")
			correct += 1
		else:
			print(f"Sorry, you missed that one. The answer is {root ** 2}.")

	print(f"You got {correct} out of 10 for a score of {(correct/10)*100}%.")

	again = input("Play again? (y/n): ")
	header()

print("\nOK. Goodbye\n")



