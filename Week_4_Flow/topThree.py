# topThree.py
# A program that generates 10 random numbers (0-100) , prints them out then prints out the top three.
# Author: Andy Walker

# Ref: Automate the Boring Stuff, Flow Control, Importing Modules, p57
import random

# Program the general case:
totalNumbers = 10
topNumbers = 3
rangeFrom = 0
rangeTo = 100

numbers = []

for i in range (totalNumbers):
    numbers.append(random.randint(rangeFrom, rangeTo))

print ("The {} random numbers are: {}".format(totalNumbers, numbers))

numbers.sort(reverse=True)

print ("The top {} numbers are: {}".format(topNumbers, numbers[0:topNumbers]))
   
    