"""
QUESTION:
Write a function `calculate_euclidean_distance` that takes a reference point and a list of points as input, and returns a list of Euclidean distances from the reference point to each point in the list. The reference point and all other points are represented as tuples of two integers.
"""

import math

def calculate_euclidean_distance(ref_point, points):
    """
    Calculate the Euclidean distances from a reference point to a list of points.

    Args:
        ref_point (tuple): The reference point as a tuple of two integers.
        points (list): A list of points, where each point is a tuple of two integers.

    Returns:
        list: A list of Euclidean distances from the reference point to each point.
    """
    return [math.sqrt(pow(point[0] - ref_point[0], 2) + pow(point[1] - ref_point[1], 2)) for point in points]