"""
QUESTION:
Create a function `euclidean_distance` that takes two tuples representing points in a 2-dimensional Cartesian coordinate system and returns the Euclidean distance between them. The points are represented as tuples with the first element being the X coordinate and the second element being the Y coordinate.
"""

import math

def euclidean_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points in a Cartesian system.
    
    Parameters:
        point1 (tuple): A 2-dimensional point in Cartesian coordinates.
        point2 (tuple): A 2-dimensional point in Cartesian coordinates.

    Returns:
        The Euclidean distance between point1 and point2.
    """
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)