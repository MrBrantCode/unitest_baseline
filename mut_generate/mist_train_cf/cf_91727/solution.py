"""
QUESTION:
Write a function named `calculate_hypotenuse` that takes two parameters: `side1` and `side2`, representing the lengths of two sides of a right triangle. The function should return the length of the hypotenuse if `side1` and `side2` form a valid right triangle; otherwise, it should return an error message. Both `side1` and `side2` must be positive numbers.
"""

import math

def calculate_hypotenuse(side1, side2):
    if side1 <= 0 or side2 <= 0:
        return "Error: The sides of a triangle must be positive numbers."
    else:
        return math.sqrt(side1**2 + side2**2)