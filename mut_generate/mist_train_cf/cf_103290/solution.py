"""
QUESTION:
Construct a function `sum_of_squares(num1, num2)` that takes two numbers as input, calculates the sum of their squares, and checks if the result is a perfect square. If the sum is a perfect square, the function should return the sum; otherwise, it should return -1.
"""

import math

def entrance(num1, num2):
    sum_squares = num1**2 + num2**2
    if math.isqrt(sum_squares) ** 2 == sum_squares:
        return sum_squares
    else:
        return -1