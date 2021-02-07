# convert.py
# A program to takes in a float amount of dollars, and returns that absolute amount in cent.
# Author: Andy Walker

dollars = float(input("Please enter an amount in dollars and cents: "))
number = abs(dollars)
cent = int(number * 100)
print ("The absolute value in cents is: {}".format(cent))