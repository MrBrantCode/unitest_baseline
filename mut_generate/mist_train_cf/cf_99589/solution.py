"""
QUESTION:
Write a function called `calculate_hypotenuse` that takes two arguments `a` and `b` representing the lengths of the legs of a right triangle. The function should return the length of the hypotenuse calculated using the Pythagorean theorem formula `c = sqrt(a^2 + b^2)`.
"""

import math

def calculate_hypotenuse(a, b):
    """
    Calculate the length of the hypotenuse of a right triangle using the Pythagorean theorem.

    Args:
        a (float): The length of the first leg of the right triangle.
        b (float): The length of the second leg of the right triangle.

    Returns:
        float: The length of the hypotenuse.
    """
    return math.sqrt(a**2 + b**2)