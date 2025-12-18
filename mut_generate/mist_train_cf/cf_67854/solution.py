"""
QUESTION:
Write a function called `pairwise_distances` that generates all pairwise distances from a given list of points `x`. The function should return a list of unique distances in ascending order, or a 2D array representing the upper triangular matrix of pairwise distances.
"""

def pairwise_distances(x):
    """
    Generate all pairwise distances from a given list of points.

    Parameters:
    x (list): A list of points.

    Returns:
    list: A list of unique distances in ascending order, or a 2D array representing the upper triangular matrix of pairwise distances.
    """
    distances = [abs(j-i) for i in x for j in x if i < j]
    return sorted(set(distances))

def pairwise_distances_matrix(x):
    """
    Generate the upper triangular matrix of pairwise distances.

    Parameters:
    x (list): A list of points.

    Returns:
    numpy.ndarray: A 2D array representing the upper triangular matrix of pairwise distances.
    """
    import numpy as np
    distances = np.abs(np.subtract.outer(x, x))
    return np.triu(distances)