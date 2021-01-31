# false.py
# A program to output whether a statement is true or false
# Author: Andy Walker

# these lines get the input
firstNumber = int(input("Please enter the first number: "))
print ("The first number is {}".format(firstNumber))
secondNumber = int(input("Please enter the second number: "))
print ("The second number is {}".format(secondNumber))

# this line provides the answer
print ("Are the numbers the same? \n{}".format(firstNumber == secondNumber))