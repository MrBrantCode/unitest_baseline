"""
QUESTION:
Write a function `calculate_hypotenuse` that takes the lengths of two legs of a right triangle as input and returns the length of the hypotenuse. Use the Pythagorean theorem formula: c = sqrt(a^2 + b^2), where c is the length of the hypotenuse, and a and b are the lengths of the legs.
"""

import math

def calculate_hypotenuse(a, b):
    """
    Calculate the length of the hypotenuse of a right triangle given the lengths of the legs.

    Args:
    a (float): The length of the first leg.
    b (float): The length of the second leg.

    Returns:
    float: The length of the hypotenuse.
    """
    return math.sqrt(a**2 + b**2)