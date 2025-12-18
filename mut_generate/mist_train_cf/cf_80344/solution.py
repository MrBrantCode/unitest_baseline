"""
QUESTION:
Write a function called `kite_height` that takes the length of a kite string and the angle it forms with the ground as input, and returns the distance from the ground to the kite. The input angle should be in degrees and the length should be in meters. Use Python's math library to compute the cosine of the angle in radians.
"""

import math

def kite_height(length, angle):
    """
    Calculate the distance from the ground to the kite.

    Parameters:
    length (float): The length of the kite string in meters.
    angle (float): The angle the kite string forms with the ground in degrees.

    Returns:
    float: The distance from the ground to the kite.
    """
    radians = math.radians(angle)
    height = length * math.cos(radians)
    return height