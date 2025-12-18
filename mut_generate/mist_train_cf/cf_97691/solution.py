"""
QUESTION:
Write a function named `euclidean_distance` that takes two tuples `point1` and `point2` as input, each representing the coordinates of a point in an n-dimensional space. The function should calculate and return the Euclidean distance between these two points as a float, handling a wide range of dimensions and providing accurate results.
"""

import math
def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points in an n-dimensional space."""
    sum_of_squares = sum([(point1[i] - point2[i]) ** 2 for i in range(len(point1))])
    return math.sqrt(sum_of_squares)