# randomFruit.py
# A program that prints out a random fruit
# Author: Andy Walker

import random

fruits = ["apple", "banana", "orange", "lemon", "melon", "strawberry"]

# the following allows more items to be added to list
# random number chosen between 0 and the length of the list minus 1
# e.g. in a four item list: (0,3) is the first 4, so if there is 4 items in list it is (0, the amount of items in the list(4) -1) =(0,3)
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print ("A random fruit: {}".format(fruit))
