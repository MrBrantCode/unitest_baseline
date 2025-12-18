"""
QUESTION:
Calculate the distance between two points in 3-dimensional space.

Write a function named `calculate_distance` to calculate the Euclidean distance between two points. The function should take two lists or tuples of three integers or floats each, representing the x, y, and z coordinates of two points in 3D space. The function should return the Euclidean distance between the two points as a float.
"""

import math

def calculate_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points in 3D space.

    Args:
        point1 (list or tuple): The x, y, and z coordinates of the first point.
        point2 (list or tuple): The x, y, and z coordinates of the second point.

    Returns:
        float: The Euclidean distance between the two points.
    """
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)