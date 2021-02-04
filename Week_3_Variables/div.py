# div.py
# A program to read in two numbers, divide the first number by the second, and give the integer result and the remainder
# Author: Andy Walker

x = int(input("Please enter the first number: "))
y = int(input("Please enter the second number: "))
print ("The integer result is: " + str(x // y))
print ("The remainder is: " + str(x % y))

# the following is a different method for the same result
print ("")
x = int(input("Please enter the first number: "))
y = int(input("Please enter the second number: "))
integer = (x // y)
remainder = (x % y)
print ("The integer result is: {}".format(integer))
print ("The remainder is: {}".format(remainder))
