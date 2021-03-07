# count.py
# A program which counts how many times it is run
# Author: Andy Walker

filename = "count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number

def writeNumber(number):
    with open(filename, "wt") as f:
        f.write(str(number))

# main
num = readNumber()
num += 1
print ("We have run this program {} times".format(num))
writeNumber(num)

