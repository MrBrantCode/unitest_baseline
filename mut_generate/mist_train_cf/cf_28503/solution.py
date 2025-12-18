"""
QUESTION:
Implement a function `manhattan_distance_matrix` that takes two input arrays `a` and `b` and returns a 2D NumPy array representing the Manhattan distance between each pair of elements from `a` and `b`. The Manhattan distance between two points (x1, y1) and (x2, y2) is defined as |x2 - x1| + |y2 - y1|. However, since only one-dimensional arrays are provided, the function should calculate the Manhattan distance as |x2 - x1|. The returned distance matrix should have the shape (len(a), len(b)).
"""

import numpy as np

def manhattan_distance_matrix(a, b):
    return np.abs(a[:, np.newaxis] - b)