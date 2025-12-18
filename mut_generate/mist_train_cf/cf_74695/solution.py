"""
QUESTION:
Create a function called `hexagon_properties` that calculates the circumference and area of a regular hexagon given the length of its side. The function should use the formulas for the circumference (6 times the side length) and area ((3 * sqrt(3) * (side ^ 2)) / 2) of a regular hexagon. The input should be the length of the side of the hexagon, and the output should be the circumference and area of the hexagon.
"""

import math

def hexagon_properties(side):
    """
    Calculate the circumference and area of a regular hexagon given the length of its side.

    Args:
        side (float): The length of the side of the hexagon.

    Returns:
        tuple: A tuple containing the circumference and area of the hexagon.
    """
    circumference = 6 * side
    area = (3 * math.sqrt(3) * (side * side)) / 2
    return circumference, area