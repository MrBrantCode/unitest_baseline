"""
QUESTION:
Calculate the height of a triangle given the length of one of its sides and an angle. Write a function `calculate_height(side_length, angle_in_degrees)` that takes in two parameters: `side_length` (the length of the side to which the angle is open) and `angle_in_degrees` (the angle value in degrees). The function should return the height of the triangle. Note that the angle value passed to the trigonometric function should be in radians, not degrees.
"""

import math

def calculate_height(side_length, angle_in_degrees):
    """
    Calculate the height of a triangle given the length of one of its sides and an angle.

    Parameters:
    side_length (float): The length of the side to which the angle is open.
    angle_in_degrees (float): The angle value in degrees.

    Returns:
    float: The height of the triangle.
    """
    angle_in_radians = math.radians(angle_in_degrees)
    height = side_length * math.sin(angle_in_radians)
    return height