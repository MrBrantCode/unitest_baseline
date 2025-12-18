"""
QUESTION:
Write a function called `euclidean_distance` that calculates the Euclidean Distance between two points in an n-dimensional space. The function should take two points as input, where each point is represented as a list of coordinates, and return the Euclidean Distance between them. The function should be able to handle an arbitrary number of dimensions for the points.
"""

import math

def euclidean_distance(point1, point2):
    squared_diff = [(point1[i] - point2[i]) ** 2 for i in range(len(point1))]
    sum_squared_diff = sum(squared_diff)
    euclidean_dist = math.sqrt(sum_squared_diff)
    return euclidean_dist