"""
QUESTION:
Implement a function `calculate_pairwise_distances` that calculates the pairwise distances between a set of 2D points. The function should take a list of 2D points as input, where each point is represented as a tuple (x, y), and return a 2D numpy array representing the distances between each pair of points. The element at position (i, j) in the output array should represent the distance between the ith and jth points in the input list. Ensure the solution is efficient and handles edge cases appropriately.
"""

import numpy as np

def calculate_pairwise_distances(points):
    """
    Calculate the pairwise distances between a set of 2D points.

    Args:
    points (list): A list of 2D points represented as tuples (x, y).

    Returns:
    np.array: A 2D array representing the distances between each pair of points.
    """
    num_points = len(points)
    embedding = np.zeros((num_points, num_points))  

    for i in range(num_points):
        for j in range(num_points):
            if i != j:  
                distance = np.linalg.norm(np.array(points[i]) - np.array(points[j]))  
                embedding[i, j] = distance  

    return embedding