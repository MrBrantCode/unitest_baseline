"""
QUESTION:
Calculate the angle of a triangle given its three sides. The function should take the lengths of the three sides of the triangle as input (a, b, and c) and return the angle in degrees opposite side c using the Law of Cosines, where the angle is calculated as C = cos^-1((a^2 + b^2 - c^2) / (2ab)). The function should be named `calculate_angle` and should not take any additional arguments other than the side lengths.
"""

import math

def calculate_angle(a, b, c):
    """
    Calculate the angle of a triangle given its three sides using the Law of Cosines.

    Args:
        a (float): The length of side a.
        b (float): The length of side b.
        c (float): The length of side c.

    Returns:
        float: The angle in degrees opposite side c.
    """
    # Calculate the angle using the Law of Cosines
    angle_in_radians = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
    
    # Convert the angle from radians to degrees
    angle_in_degrees = math.degrees(angle_in_radians)
    
    return angle_in_degrees