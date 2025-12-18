"""
QUESTION:
Write a function called `calculate_hypotenuse` that takes in two arguments representing the lengths of the sides of a right-angled triangle. The function should return the length of the hypotenuse rounded to the nearest whole number using the Pythagorean theorem.
"""

import math

def calculate_hypotenuse(side1, side2):
    return round(math.sqrt(side1 ** 2 + side2 ** 2))