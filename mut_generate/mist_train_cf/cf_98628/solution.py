"""
QUESTION:
Write a Python function named `calculate_hypotenuse` that calculates the length of the hypotenuse of a right triangle given the lengths of its legs. The function should use the Pythagorean theorem formula (c = sqrt(a^2 + b^2)) and should take two parameters representing the lengths of the legs.
"""

import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)