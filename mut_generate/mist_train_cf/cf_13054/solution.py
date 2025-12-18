"""
QUESTION:
Implement a function named `calculate_new_centroid` that takes a cluster of n-dimensional points as input and returns the centroid of the cluster. The centroid should be calculated by finding the mean along each dimension separately.
"""

def calculate_new_centroid(cluster):
    # Calculate mean of each dimension separately
    dimensions = len(cluster[0])
    centroid = [0] * dimensions

    for i in range(dimensions):
        centroid[i] = sum([point[i] for point in cluster]) / len(cluster)

    return centroid