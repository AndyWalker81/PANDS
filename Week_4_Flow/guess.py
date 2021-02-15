# guess.py
# A program that prompts the user to guess a number and keep prompting unless the user guesses correctly
# Author: Andy Walker

numberToGuess = 50

userGuess = int(input("Please guess a number: "))

while userGuess != numberToGuess:
    userGuess = int(input("Incorrect. Please guess again: "))
print ("Correct. The number was {}".format(numberToGuess))