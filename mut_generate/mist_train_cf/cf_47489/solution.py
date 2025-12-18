"""
QUESTION:
Calculate the slant height of a pyramid with a square base and an apex perpendicular to the center of the square base. The length of one side of the square base and the pyramid's height are given. Implement the Pythagorean theorem for three dimensions to find the slant height.

Function name: calculate_slant_height
Input parameters: base_length (the length of one side of the square base), height (the pyramid's height)
Restrictions: The pyramid's apex is perpendicular to the center of the square base.
"""

import math

def calculate_slant_height(base_length, height):
    """
    Calculate the slant height of a pyramid with a square base and an apex perpendicular to the center of the square base.

    Args:
        base_length (float): The length of one side of the square base.
        height (float): The pyramid's height.

    Returns:
        float: The slant height of the pyramid.
    """
    # Calculate half of the base
    half_base = base_length / 2
    
    # Apply the Pythagorean theorem in three dimensions to determine the slant height
    slant_height = math.sqrt(half_base**2 + height**2)
    
    return slant_height