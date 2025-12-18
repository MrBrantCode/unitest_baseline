"""
QUESTION:
Write a function `calculate_distance` that calculates the Euclidean distance between two points in a 3D coordinate system and returns the distance rounded to the nearest integer. The function should take two parameters, `point1` and `point2`, where each point is a tuple of three numbers representing the x, y, and z coordinates.
"""

import math

def calculate_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points in a 3D coordinate system.

    Args:
    point1 (tuple): A tuple of three numbers representing the x, y, and z coordinates.
    point2 (tuple): A tuple of three numbers representing the x, y, and z coordinates.

    Returns:
    int: The Euclidean distance between the two points rounded to the nearest integer.
    """
    return round(math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2))