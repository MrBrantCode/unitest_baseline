"""
QUESTION:
Calculate the height of a triangle given the angle, side lengths, and opposite side length. Implement a function named `calculate_triangle_height` that takes in three parameters: `opposite_side_length`, `side_length`, and `angle_in_degrees`. The function should return the calculated height. The angle is expected to be in degrees, not radians.
"""

import math

def calculate_triangle_height(opposite_side_length, side_length, angle_in_degrees):
    """
    Calculate the height of a triangle given the opposite side length, side length, and angle in degrees.

    Args:
        opposite_side_length (float): The length of the side opposite the angle.
        side_length (float): The length of the side adjacent to the angle.
        angle_in_degrees (float): The angle in degrees.

    Returns:
        float: The calculated height of the triangle.
    """
    angle_in_radians = math.radians(angle_in_degrees)
    return opposite_side_length * math.sin(angle_in_radians) / side_length