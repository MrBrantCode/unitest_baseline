"""
QUESTION:
Implement the function `k_means_clustering(data, k, max_iterations=100)` that groups a given dataset into k distinct clusters using the k-means clustering algorithm. The function should take as input a 2D numpy array `data` representing the dataset, an integer `k` representing the number of clusters, and an optional integer `max_iterations` representing the maximum number of iterations (default is 100). The function should return a tuple containing a 1D numpy array `clusters` representing the cluster assignment for each data point and a 2D numpy array `centroids` representing the coordinates of the k centroids. The implementation should not use any built-in libraries or functions that directly implement the k-means algorithm.
"""

import numpy as np

def k_means_clustering(data, k, max_iterations=100):
    # Initialize centroids randomly
    centroids = initialize_centroids(data, k)
    
    for _ in range(max_iterations):
        # Assign each data point to the nearest centroid
        clusters = assign_points_to_centroids(data, centroids)
        
        # Update the centroids
        new_centroids = update_centroids(data, clusters, k)
        
        # Check if convergence is reached
        if np.allclose(centroids, new_centroids):
            break
        
        centroids = new_centroids
    
    return clusters, centroids

def initialize_centroids(data, k):
    n_samples, _ = data.shape
    centroids_indices = np.random.choice(n_samples, k, replace=False)
    centroids = data[centroids_indices]
    return centroids

def assign_points_to_centroids(data, centroids):
    n_samples, _ = data.shape
    clusters = np.zeros(n_samples)
    for i in range(n_samples):
        distances = np.linalg.norm(data[i] - centroids, axis=1)
        cluster = np.argmin(distances)
        clusters[i] = cluster
    return clusters

def update_centroids(data, clusters, k):
    n_features = data.shape[1]
    new_centroids = np.zeros((k, n_features))
    for cluster in range(k):
        cluster_points = data[clusters == cluster]
        if cluster_points.shape[0] > 0:
            new_centroids[cluster] = np.mean(cluster_points, axis=0)
    return new_centroids