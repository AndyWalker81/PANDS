# queue.py
# A program to count down a queue of random numbers
# Author: Andy Walker

import random

queue = []

while (len(queue) < 10):
    queue.append(random.randint(0,101))

print ("The queue is: {}".format(queue))

while (len(queue) != 0):
    updatedQueue = queue.pop(0)

    print ("The current number is {} and the queue is: {}".format(updatedQueue, queue))

