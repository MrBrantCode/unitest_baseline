"""
QUESTION:
Write a function `sum_of_squares(a, b)` that takes two parameters and returns the sum of their squares if the sum is a perfect square, otherwise returns -1. The function should have a time complexity of O(1) and a space complexity of O(1).
"""

import math

def sum_of_squares(a, b):
    # calculate the sum of squares
    sum_of_squares = a**2 + b**2
    
    # check if the sum of squares is a perfect square
    if math.isqrt(sum_of_squares)**2 == sum_of_squares:
        return sum_of_squares
    else:
        return -1