"""
QUESTION:
Write a function `calculate_hypotenuse` that takes two floating point numbers as input representing the lengths of the sides of a right-angled triangle and returns the length of the hypotenuse, rounded to 3 decimal places.
"""

import math

def calculate_hypotenuse(x, y):
    return round(math.sqrt(x**2 + y**2), 3)