# guess3.py
# A program that prompts the user to guess a randomly generated number and keep prompting unless the user guesses correctly.
# The program will give a clue if the guess is too high or too low
# Author: Andy Walker

# import function
from random import randint

# generator number
numberToGuess = randint(1,101)

userGuess = int(input("Please guess a number between 1 and 100: "))

while userGuess != numberToGuess:
    if userGuess > numberToGuess:
         userGuess = int(input("Your guess is too high. Please guess again: "))

    else:
        userGuess = int(input("Your guess is too low. Please guess again: "))

print ("Correct. The number was {}".format(numberToGuess))