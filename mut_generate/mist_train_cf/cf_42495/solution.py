"""
QUESTION:
Write a function `calculate_pairwise_distances(antpos)` that takes a 2D NumPy array `antpos` containing the x, y, z positions of antennas as input and returns a 2D array representing the pairwise distances between antennas. The distance between two points in 3D space can be calculated using the Euclidean distance formula. The function should handle the calculation of distances for all possible pairs of antennas and return the distances in a 2D array.
"""

import numpy as np

def entrance(antpos):
    num_antennas = antpos.shape[0]
    pairwise_distances = np.zeros((num_antennas, num_antennas))

    for i in range(num_antennas):
        for j in range(num_antennas):
            if i != j:
                distance = np.linalg.norm(antpos[i] - antpos[j])
                pairwise_distances[i, j] = distance

    return pairwise_distances