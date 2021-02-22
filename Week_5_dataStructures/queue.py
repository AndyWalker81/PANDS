# queue.py
# A program to count down a queue of random numbers
# Author: Andy Walker

import random

queue = []
x = 10
y = 100

# the next lines are my method:
#while (len(queue) < x):
#    queue.append(random.randint(0,y))

# the next lines are Andrew's method
for n in range(0,x):
    queue.append(random.randint(0,y))

print ("The queue is: {}".format(queue))

while (len(queue) != 0):
    updatedQueue = queue.pop(0)

    print ("The current number is {} and the queue is: {}".format(updatedQueue, queue))

