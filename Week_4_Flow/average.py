# average.py
# A program that keeps reading numbers until the user enters a 0. 
# The program will then print out each of the numbers entered and the averages of them.
# Author: Andy Walker

numbers = []

number = int(input("Please enter a number (0 to quit): "))

while number != 0:
    numbers.append(number)
    number = int(input("enter another (0 to quit): "))

for value in numbers:
    print (value)

mean = float(sum(numbers)) / len(numbers)
print ("The average is: {}".format(mean))