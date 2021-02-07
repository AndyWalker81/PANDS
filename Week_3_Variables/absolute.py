# absolute.py
# A program to take in a number and give its absolute value (i.e. -4 or 4 would both output 4) as a float
# Author: Andy Walker

number = int(input("Please enter either a positive or negative integer: "))
answer = float(abs(number))
print ("The absolute value is: {}".format(answer))