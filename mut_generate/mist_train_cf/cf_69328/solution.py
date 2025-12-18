"""
QUESTION:
Implement a custom DBSCAN algorithm that clusters data points based on a given distance matrix, epsilon value, and minimum sample size. The algorithm should assign noise points to a special cluster labeled -1. The function should be able to handle different epsilon and minimum sample values without modification. It should also calculate the average silhouette score of the clusters.

The function, named `dbscan`, should take three inputs: `distance_matrix` (a 2D array of pairwise distances between data points), `eps` (the maximum distance between points in a cluster), and `min_samples` (the minimum number of points required to form a dense region). The function should return an array of labels, where each label corresponds to a cluster assignment for a data point.
"""

import numpy as np

def dbscan(distance_matrix, eps, min_samples):
    labels = np.full(distance_matrix.shape[0], np.inf)
    cluster_id = 0

    for point_index in range(distance_matrix.shape[0]):
        if labels[point_index] != np.inf:
            continue

        neighbors = np.where(distance_matrix[point_index] < eps)[0]
        if neighbors.shape[0] < min_samples:
            labels[point_index] = -1
            continue

        labels[point_index] = cluster_id
        cluster_points = list(neighbors)
        j = 0

        while j < len(cluster_points):
            current_point_index = cluster_points[j]
            j += 1
            
            if labels[current_point_index] == -1:
                labels[current_point_index] = cluster_id

            if labels[current_point_index] != np.inf:
                continue

            labels[current_point_index] = cluster_id
            neighbors = np.where(distance_matrix[current_point_index] < eps)[0]

            if neighbors.shape[0] >= min_samples:
                cluster_points.extend(list(neighbors))
                
        cluster_id += 1
        
    return labels