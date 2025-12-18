"""
QUESTION:
Calculate the area of a regular octagon whose distance from its center to each vertex is provided as an integer ranging from 1 cm to 20 cm. The function should be named `calculate_octagon_area`. If possible, use this distance to generate a 2D plot of the regular octagon using matplotlib library.
"""

import math

def calculate_octagon_area(distance):
    """
    Calculate the area of a regular octagon.

    Args:
    distance (int): The distance from the center to each vertex of the octagon.

    Returns:
    float: The area of the regular octagon.
    """
    return 2 * distance ** 2 * (1 + math.sqrt(2))