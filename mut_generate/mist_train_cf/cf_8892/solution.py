"""
QUESTION:
Write a function `calculate_height` that calculates the height of a triangle given the angle and side lengths. The function should take two parameters: the angle in radians and the side length opposite to the angle.
"""

import math

def calculate_height(angle, side_length):
    """
    Calculate the height of a triangle given the angle and side length.

    Parameters:
    angle (float): The angle in radians.
    side_length (float): The length of the side opposite to the angle.

    Returns:
    float: The height of the triangle.
    """
    return side_length * math.sin(angle)