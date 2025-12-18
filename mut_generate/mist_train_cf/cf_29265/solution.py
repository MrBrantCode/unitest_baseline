"""
QUESTION:
Write a function `find_min_class(X, X_0)` that finds the index of the point in `X_0` with the minimum Euclidean distance to point `X` in a multi-dimensional space.

- `X` is a numpy array representing a single point in the multi-dimensional space.
- `X_0` is a numpy array representing a set of points in the multi-dimensional space.
- The function should use `np.linalg.norm` to calculate the Euclidean distance between two points.
- The function should return the index of the point in `X_0` with the minimum Euclidean distance to point `X`.
"""

import numpy as np

def find_min_class(X, X_0):
    """
    This function finds the index of the point in X_0 with the minimum Euclidean distance to point X.

    Parameters:
    X (numpy array): A single point in the multi-dimensional space.
    X_0 (numpy array): A set of points in the multi-dimensional space.

    Returns:
    int: The index of the point in X_0 with the minimum Euclidean distance to point X.
    """
    min_distance = np.inf
    min_class = 0

    for idx in range(len(X_0)):
        dist = np.linalg.norm(X - X_0[idx])
        if dist < min_distance:
            min_distance = dist
            min_class = idx

    return min_class