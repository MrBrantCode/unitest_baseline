"""
QUESTION:
Write a function named `calculate_hypotenuse` that takes two parameters representing the lengths of the legs of a right triangle, and returns the length of the hypotenuse calculated using the Pythagorean theorem formula. The formula is c = sqrt(a^2 + b^2), where c is the length of the hypotenuse and a and b are the lengths of the legs.
"""

import math

def calculate_hypotenuse(a, b):
    """
    Calculate the length of the hypotenuse of a right triangle using the Pythagorean theorem.
    
    Parameters:
    a (float): The length of one leg of the right triangle.
    b (float): The length of the other leg of the right triangle.
    
    Returns:
    float: The length of the hypotenuse of the right triangle.
    """
    return math.sqrt(a**2 + b**2)