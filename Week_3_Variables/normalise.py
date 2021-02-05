# normalise.py
# A program that reads in a string and strips any leading or trailing spaces
# It also converts the string to lower case. 
# It also outputs the length of the input and output strings.
# Author: Andy Walker

rawString = input("Please enter a piece of text, including capital letters: ")
normalisedString = rawString.strip().lower()

lengthOfRawString = len(rawString)
lengthOfNormalised = len(normalisedString)

print ("The text in lower case is: {}".format(normalisedString))
print ("We reduced the input string from {} to {} characters: ".format (lengthOfRawString, lengthOfNormalised ))