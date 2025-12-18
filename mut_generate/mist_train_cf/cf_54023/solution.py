"""
QUESTION:
Write a function `square_area` that takes a diagonal length of a square as an argument and returns the area of the square using recursion, without directly using the mathematical formula for the area of a square.
"""

import math

def square_area(diagonal, n=2): 
    if n == 0:
        return diagonal
    else:
        return square_area(diagonal / math.sqrt(2), n - 1) ** 2