"""
QUESTION:
Create a function named `euclidean_distance` that calculates the Euclidean distance between two points in a 3D coordinate system. The function should take two tuples or lists of three numbers each, representing the x, y, and z coordinates of the two points, and return the calculated distance.
"""

import math

def euclidean_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points in a 3D coordinate system.

    Args:
    point1 (tuple or list): The x, y, and z coordinates of the first point.
    point2 (tuple or list): The x, y, and z coordinates of the second point.

    Returns:
    float: The Euclidean distance between the two points.
    """
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)