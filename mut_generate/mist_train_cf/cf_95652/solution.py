"""
QUESTION:
Create a function called `cube` that calculates the cube of a given number using only addition and multiplication operations. The function should work for both positive and negative numbers.
"""

def cube(number):
    result = 0
    if number < 0:
        sign = -1
    else:
        sign = 1

    number = abs(number)
    result = number * number
    result = result * number

    return sign * result