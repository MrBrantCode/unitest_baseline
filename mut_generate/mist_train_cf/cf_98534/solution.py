"""
QUESTION:
Write a function `equilateral_triangle_height` that calculates the height of an equilateral triangle given the length of one side. The function should return the calculated height. The input will be a single number representing the side length of the equilateral triangle. The output should be the calculated height of the equilateral triangle.
"""

import math

def equilateral_triangle_height(side_length):
    """
    Calculate the height of an equilateral triangle given the length of one side.

    Args:
        side_length (float): The length of one side of the equilateral triangle.

    Returns:
        float: The calculated height of the equilateral triangle.
    """
    return (math.sqrt(3) / 2) * side_length