"""
QUESTION:
Calculate the angle of elevation for a ball thrown upward with an initial velocity. 

The function `calculate_angle` should take one argument, the initial velocity of the ball in m/s, and return the angle of elevation in degrees. Assume the acceleration due to gravity is 9.8 m/s^2.
"""

import math

def calculate_angle(velocity):
    """
    Calculate the angle of elevation for a ball thrown upward with an initial velocity.

    Args:
    velocity (float): The initial velocity of the ball in m/s.

    Returns:
    float: The angle of elevation in degrees.
    """
    return math.degrees(math.atan(velocity / 9.8))