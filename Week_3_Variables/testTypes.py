# testTypes.py
# A program to list types of variable
# Author: Andy Walker

# the following are five types of variable
a = 1
b = 1.1
c = True
d = 'hello'
e = []

# the following lines output the type of variable and the value of the variable
print ("variable a is of type: " + str(type(a)) + " and value: " + str(a))
print ("variable b is of type: " + str(type(b)) + " and value: " + str(b))
print ("variable c is of type: " + str(type(c)) + " and value: " + str(c))
print ("variable d is of type: " + str(type(d)) + " and value: " + str(d))
print ("variable e is of type: " + str(type(e)) + " and value: " + str(e))

# the following lines out the type of variable and the value of the variable using a different way of coding
print ("")
print ("variable {} is of type: {} and value: {}".format('a', type(a), a))
print ("variable {} is of type: {} and value: {}".format('b', type(b), b))
print ("variable {} is of type: {} and value: {}".format('c', type(c), c))
print ("variable {} is of type: {} and value: {}".format('d', type(d), d))
print ("variable {} is of type: {} and value: {}".format('e', type(e), e))