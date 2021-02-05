# randomGenerator.py
# A program that prints out a random number from a range inputed by the user
# Author: Andy Walker

# import the module random
import random

# user enters the range
x = int(input("Please enter the first number: "))
y = int(input("Please enter the second number: "))

# print a random number from the range input
number = random.randint(x,y)
print("Here is a random number: {}".format(number))