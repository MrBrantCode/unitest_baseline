"""
QUESTION:
Write a function called `calculate_sine` that takes an angle in degrees as input and returns its sine value. The angle should be converted from degrees to radians before calculating the sine, and the function should return the result. The input angle is expected to be a numeric value.
"""

import math

def calculate_sine(angle):
    """
    Calculate the sine of an angle in degrees.

    Args:
    angle (float): The angle in degrees.

    Returns:
    float: The sine of the angle.
    """
    return math.sin(math.radians(angle))