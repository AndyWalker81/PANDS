#  grade2.py
# A program to read a student's percentage mark and print out the corresponding grade using rounding
# Author: Andy Walker

mark = float(input("Please enter the percentage mark: "))

# rounds to one decimal place
markRounded = round(mark, 0)
print (markRounded)

if (markRounded <= 40):
    print ("{} is a Fail".format(mark))
elif (markRounded >= 40 and mark <= 49):
    print ("{} is a Pass".format(mark))
elif (markRounded >= 50 and mark <= 59):
    print ("{} is a Merit 2".format(mark))
elif (markRounded >= 60 and mark <= 69):
    print ("{} is a Merit 1".format(mark))

# the only option left is a distinction
else:
    print ("{} is a Distinction".format(mark))