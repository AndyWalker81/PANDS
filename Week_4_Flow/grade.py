# grade.py
# A program to read a student's percentage mark and print out the corresponding grade
# Author: Andy Walker

mark = int(input("Please enter the percentage mark: "))

if (mark < 40):
    print ("{} is a Fail".format(mark))
elif (mark >= 40 and mark <= 49):
    print ("{} is a Pass".format(mark))
elif (mark >= 50 and mark <= 59):
    print ("{} is a Merit 2".format(mark))
elif (mark >= 60 and mark <= 69):
    print ("{} is a Merit 1".format(mark))

# the only option left is a distinction
else:
    print ("{} is a Distinction".format(mark))
