"""
QUESTION:
Write a function `euclidean_distance(point1, point2)` that calculates the Euclidean Distance between two points in an n-dimensional space. The points are represented as lists of numbers. The function should be able to handle points with any number of dimensions.
"""

import math

def euclidean_distance(point1, point2):
    """
    Calculate the Euclidean Distance between two points in an n-dimensional space.
    
    Args:
        point1 (list): The first point, represented as a list of numbers.
        point2 (list): The second point, represented as a list of numbers.
    
    Returns:
        float: The Euclidean Distance between the two points.
    """
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(point1, point2)]))
    return distance