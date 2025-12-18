"""
QUESTION:
Create a function `degToRad(deg)` that takes an angle in degrees as input and returns the equivalent angle in radians. The function should use the mathematical constant PI and follow the formula `radians = degrees * (PI/180)`.
"""

import math

def deg_to_rad(deg):
    """
    Convert an angle from degrees to radians.
    
    Parameters:
    deg (float): The angle in degrees.
    
    Returns:
    float: The equivalent angle in radians.
    """
    return deg * (math.pi/180)