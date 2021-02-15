# guess2.py
# A program that prompts the user to guess a number and keep prompting unless the user guesses correctly.
# The program will give a clue if the number is too high or too low
# Author: Andy Walker

numberToGuess = 100

userGuess = int(input("Please guess a number: "))

while userGuess != numberToGuess:
    if userGuess > numberToGuess:
         userGuess = int(input("Your guess is too high. Please guess again: "))

    else:
        userGuess = int(input("Your guess is too low. Please guess again: "))

print ("Correct. The number was {}".format(numberToGuess))