# isEven.py
# A program to determine if a number is odd or even
# Author: Andy Walker

number = int(input("Please enter a number: "))

if (number % 2) == 0:
    print ("{} is an even number".format(number))
else:   
    print ("{} is an odd number".format(number))