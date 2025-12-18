"""
QUESTION:
Write a function named `euclidean_distance` that calculates the Euclidean distance between two points in a multi-dimensional space. The function should take two lists of equal length, representing the coordinates of the two points, as input and return the Euclidean distance as output. The function must use the NumPy library.
"""

import numpy as np

def euclidean_distance(point1, point2):
    point1, point2 = np.array(point1), np.array(point2)
    return np.sqrt(np.sum((point1 - point2) ** 2))