"""
QUESTION:
Write a function `calculate_hypotenuse` that takes two arguments `side1` and `side2` representing the lengths of two sides of a right triangle. The function should return the length of the hypotenuse if the sides form a valid right triangle and an error message otherwise. The sides of a valid triangle must be positive numbers and must satisfy the Pythagorean theorem.
"""

import math

def calculate_hypotenuse(side1, side2):
    if side1 <= 0 or side2 <= 0:
        return "Error: The sides of a triangle must be positive numbers."
    else:
        hypotenuse = math.sqrt(side1**2 + side2**2)
        return hypotenuse