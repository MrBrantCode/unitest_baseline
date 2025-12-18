"""
QUESTION:
Write a function `power_func(number)` that takes an integer as input. If the input number is non-negative, the function should return the square of the number. If the input number is negative, the function should return the absolute value of the number multiplied by the factorial of its absolute value.
"""

import math

def power_func(number):
    if number >= 0:
        return number**2
    else:
        return abs(number) * math.factorial(abs(number))