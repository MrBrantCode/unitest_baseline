"""
QUESTION:
Implement a function named `euclidean_distance` that takes two tuples of numbers, `point1` and `point2`, as input and returns the Euclidean distance between these two points in n-dimensional space as a float. The function should be able to handle a wide range of dimensions and provide accurate results. Use list comprehension in the implementation.
"""

import math
def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points in an n-dimensional space."""
    sum_of_squares = sum([(point1[i] - point2[i]) ** 2 for i in range(len(point1))])
    return math.sqrt(sum_of_squares)