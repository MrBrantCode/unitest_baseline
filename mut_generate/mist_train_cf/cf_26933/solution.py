"""
QUESTION:
Implement a function `calculate_vertex_distances(n)` that takes an integer `n` as input and returns a 2D array representing the distances between vertices of a sphere with `n` vertices. The distance between vertex `i` and vertex `j` should be stored in `distances[i][j]` and `distances[j][i]`, where `i` and `j` are the indices of the vertices. The distance between a vertex and itself should be 0.
"""

import numpy as np

def calculate_vertex_distances(n):
    distances = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            distance = calculate_distance_between_vertices(i, j)  # Replace with actual distance calculation function
            distances[i][j] = distance
            distances[j][i] = distance
    return distances

def calculate_distance_between_vertices(i, j):
    # Replace with actual distance calculation function
    # For demonstration purposes, this example uses a simple difference
    return abs(i - j)