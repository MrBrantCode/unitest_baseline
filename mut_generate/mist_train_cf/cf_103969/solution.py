"""
QUESTION:
Calculate the Euclidean distance between the origin point and each point in a set. The function should be named `euclidean_distance` and take in a list of tuples representing the points and a tuple representing the origin point. The function should return a list of floats representing the Euclidean distance between the origin point and each point in the set. Assume that the points are in 2D space, represented as (x, y) coordinates.
"""

import math

def euclidean_distance(points, origin):
    """
    Calculate the Euclidean distance between the origin point and each point in a set.

    Args:
        points (list of tuples): A list of points in 2D space, represented as (x, y) coordinates.
        origin (tuple): The origin point in 2D space, represented as (x, y) coordinates.

    Returns:
        list of floats: A list of Euclidean distances between the origin point and each point in the set.
    """
    return [math.sqrt((x - origin[0]) ** 2 + (y - origin[1]) ** 2) for x, y in points]