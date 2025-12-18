"""
QUESTION:
Write a function called `calculate_hypotenuse` to calculate the length of the hypotenuse of a right triangle given the lengths of its legs, using the Pythagorean theorem formula: c = sqrt(a^2 + b^2), where c is the length of the hypotenuse and a and b are the lengths of the legs. The function should take two arguments, the lengths of the two legs, and return the length of the hypotenuse.
"""

import math

def calculate_hypotenuse(a, b):
    """
    Calculate the length of the hypotenuse of a right triangle given the lengths of its legs.

    Args:
        a (float): The length of one leg.
        b (float): The length of the other leg.

    Returns:
        float: The length of the hypotenuse.
    """
    return math.sqrt(a**2 + b**2)