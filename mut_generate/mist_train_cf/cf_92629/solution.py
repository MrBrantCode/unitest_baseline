"""
QUESTION:
Implement a function named `calculate_new_centroid` that calculates the mean of each dimension of a given cluster in a K-means clustering algorithm. The cluster is a list of data points, where each data point is a list of coordinates. The function should return a new centroid, which is a list of mean coordinates. The input cluster may contain duplicate points and the number of dimensions in each point is consistent but unknown.
"""

def calculate_new_centroid(cluster):
    # Calculate mean of each dimension separately
    dimensions = len(cluster[0])
    centroid = [0] * dimensions

    for i in range(dimensions):
        centroid[i] = sum([point[i] for point in cluster]) / len(cluster)

    return centroid