"""
QUESTION:
Write a function `euclidean_distance(point1, point2)` that takes two tuples as input, each representing the coordinates of a point in an n-dimensional space, and returns a float representing the Euclidean distance between these points. The function should be able to handle a wide range of dimensions and provide accurate results. Implement this function using list comprehension.
"""

import math
def euclidean_distance(point1, point2):
 """Calculate the Euclidean distance between two points in an n-dimensional space."""
 sum_of_squares = sum([(point1[i] - point2[i]) ** 2 for i in range(len(point1))])
 return math.sqrt(sum_of_squares)