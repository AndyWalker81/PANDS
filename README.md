# PANDS
Programming and Scripting

31/1/21
Create Week_2 folder in Git Hub
Push 7 programs to it from the lab 

4/2/21
Creat Week_3_Variables folder in Git Hub
Push 3 programs to it from the lab

5/2/21
Push 3 more programs to Week_3_Variables folder from the lab

7/2/21 
Push 4 more programs to Week_3_Variables folder from the lab

8/2/21
Push final 1 program to Week_3_Variables folder from the lab

12/2/21
Create Week_4_Flow folder in Git Hub
Push 2 programs to it from the lab

15/2/21
Push 4 programs to Week_4_Flow folder from the lab

16/2/21
Push 4 programs to Week_4_Flow folder from the lab

17/2/21
Push final 1 program to Week_4_Flow folder from the lab
Push collatzList.py to this folder - this is different method for Week 4 task:

# collatz.py
# Week 4 task
# A program that asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step it calculates the next value by taking the current value
# If it is even, it divides it by two
# If it is odd, it multiplies it by three and add one.
# The program ends if the value is one.
# Author: Andy Walker

number = int(input("Please enter a positive integer: "))

# creates a list
numbers = []

# The append() method appends an element to the end of the list.
# Reference: https://www.w3schools.com/python/ref_list_append.asp

numbers.append(number)

# Runs a loop while the number is not equal to 1
# Each number is added to this numbers list using append method
while number != 1:
    if number % 2 == 0:
        number = int(number / 2)
        numbers.append(number)
    else:
        number = int(number * 3  + 1)
        numbers.append(number)

# print the number list
# The end key avoids a new line
# Reference: https://stackoverflow.com/questions/12032214/print-new-output-on-same-line
for value in numbers:
    print (value, end = ' ')



