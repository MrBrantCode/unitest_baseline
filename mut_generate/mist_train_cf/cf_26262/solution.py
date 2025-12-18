"""
QUESTION:
Write a function called `points_distance` that takes two inputs: a list of points where each point is a tuple of two numbers, and an origin point which is also a tuple of two numbers. The function should return a list of distances from the origin point to each point in the input list, calculated using the Euclidean distance formula.
"""

import math

def points_distance(points, origin):
    """
    Calculate the Euclidean distance from the origin point to each point in the input list.

    Args:
    points (list): A list of points where each point is a tuple of two numbers.
    origin (tuple): The origin point which is a tuple of two numbers.

    Returns:
    list: A list of distances from the origin point to each point in the input list.
    """
    return [math.sqrt((point[0]-origin[0])**2 + (point[1]-origin[1])**2) for point in points]