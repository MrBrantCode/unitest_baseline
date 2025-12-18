"""
QUESTION:
Write a function `calculate_angle` that takes four parameters: the X and Y coordinates of two points. The function should return the angle in degrees between the two points. The angle should be calculated using the arctangent function, with the Y difference as the first argument and the X difference as the second argument.
"""

import math

def calculate_angle(x1, y1, x2, y2):
    """
    Calculate the angle in degrees between two points.

    Args:
        x1 (float): The X coordinate of the first point.
        y1 (float): The Y coordinate of the first point.
        x2 (float): The X coordinate of the second point.
        y2 (float): The Y coordinate of the second point.

    Returns:
        float: The angle in degrees between the two points.
    """
    delta_y = y2 - y1
    delta_x = x2 - x1
    angle_in_degrees = (math.atan2(delta_y, delta_x)) * 180 / math.pi
    return angle_in_degrees