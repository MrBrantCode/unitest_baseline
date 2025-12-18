"""
QUESTION:
Write a function `square_perimeter` that calculates the perimeter of a square inscribed in a circle with a given diameter. The function should take the diameter of the circle as an argument and return the perimeter of the square in terms of pi.
"""

import math

def square_perimeter(diameter):
    """
    Calculate the perimeter of a square inscribed in a circle.

    Parameters:
    diameter (float): The diameter of the circle.

    Returns:
    float: The perimeter of the square in terms of pi.
    """
    side_length = math.sqrt((diameter ** 2) / 2)
    perimeter = 4 * side_length
    return perimeter