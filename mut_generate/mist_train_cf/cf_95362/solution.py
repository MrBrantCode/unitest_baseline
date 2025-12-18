"""
QUESTION:
Create a function called "isEvenlyDivisible" that takes two integers as parameters and returns a boolean value. The function should return true if the first integer is evenly divisible by the second integer and both integers are positive. The function should also return false if the second integer is equal to 0, regardless of the first integer's value.
"""

def isEvenlyDivisible(num1, num2):
    if num2 == 0:
        return False
    elif num1 % num2 == 0 and num1 > 0 and num2 > 0:
        return True
    else:
        return False