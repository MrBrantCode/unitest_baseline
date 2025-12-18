"""
QUESTION:
Write a function `inner_square_properties` that calculates the side length and area of an inner square constructed inside an outer square with a variable side length X cm, where the diagonals of the inner square coincide with the sides of the outer square. The function should accept a single argument X, which can be an integer or floating point number, and return the side length and area of the inner square.
"""

import math

def inner_square_properties(x):
    a = x / math.sqrt(2)  # side length of the inner square
    area = a ** 2  # area of the inner square

    return a, area