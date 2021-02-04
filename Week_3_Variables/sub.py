# sub.py
# A program to read in two numbers and subtract the first one from the second one
# Author: Andy Walker

x = int(input("Please enter the first number: "))
y = int(input("Please enter the second number: "))
print ("The answer is: " + str(x - y))

# the following is a different method for the same result
print ("")
x = int(input("Please enter the first number: "))
y = int(input("Please enter the second number: "))
answer = x - y
print ("The answer is: {}".format(answer))
