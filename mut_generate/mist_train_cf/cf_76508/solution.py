"""
QUESTION:
Given a right triangle with side lengths a and b, and a square inscribed within the triangle where the square's diagonal coincides with the triangle's hypotenuse, write a function `find_square_side_length` that takes a and b as input and returns the side length of the square.
"""

import math

def find_square_side_length(a, b):
    """
    Calculate the side length of a square inscribed in a right triangle.

    Args:
        a (float): The length of one side of the right triangle.
        b (float): The length of the other side of the right triangle.

    Returns:
        float: The side length of the inscribed square.
    """
    # Calculate the length of the hypotenuse (diagonal of the square)
    hypotenuse = math.sqrt(a**2 + b**2)
    
    # Calculate the side length of the square using the formula s = d / sqrt(2)
    square_side_length = hypotenuse / math.sqrt(2)
    
    return square_side_length