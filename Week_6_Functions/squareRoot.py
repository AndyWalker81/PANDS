# squareRoot.py
# Author: Andy Walker

# reference: https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d
# reference: https://www.w3schools.com/python/ref_func_round.asp
# reference: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
# reference: https://www.school-for-champions.com/algebra/square_root_approx.htm#.YD3x8tynxPa


def sqrt(number, iterations = 100):
    a = float(number)
    for i in range(iterations):
        number = 0.5 * (number + a / number)
    return number

n = float(input("Please enter a number: "))

answer = (sqrt(n))
print ("The estimated square root is: {}".format(round(answer,1)))

