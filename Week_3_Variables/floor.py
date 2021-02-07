# floor.py
# A program that takes in a float and outputs an int rounded down
# This requires the math module math.floor() which rounds a number downwards to its nearest integer
# Author: Andy Walker

import math

number = float(input("Please enter a float: "))
answer = (math.floor(number))
print ("The floor is: {}".format(answer))
