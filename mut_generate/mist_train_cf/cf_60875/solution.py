"""
QUESTION:
Create a function called `agglomerative_clustering` that groups a set of n-dimensional vectors into clusters based on their similarity. The function should take two parameters: `vectors`, a list of n-dimensional vectors representing the objects to be clustered, and `k`, the desired number of clusters. The function should use Euclidean distance as the similarity measure and return a list of clusters, where each cluster is a list of vectors.
"""

import numpy as np

def agglomerative_clustering(vectors, k):
    """
    This function groups a set of n-dimensional vectors into clusters based on their similarity.
    
    Parameters:
    vectors (list): A list of n-dimensional vectors representing the objects to be clustered.
    k (int): The desired number of clusters.
    
    Returns:
    list: A list of clusters, where each cluster is a list of vectors.
    """

    # Initialize the dataset
    num_vectors = len(vectors)
    
    # Initialize each vector as its own cluster
    clusters = [[vector] for vector in vectors]
    
    while len(clusters) > k:
        # Calculate the Euclidean distances between all pairs of clusters
        min_distance = float('inf')
        closest_clusters = None
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                distance = np.linalg.norm(np.mean(clusters[i], axis=0) - np.mean(clusters[j], axis=0))
                if distance < min_distance:
                    min_distance = distance
                    closest_clusters = (i, j)
        
        # Merge the closest pair of clusters into a single cluster
        cluster1, cluster2 = closest_clusters
        clusters[cluster1].extend(clusters[cluster2])
        del clusters[cluster2]
    
    return clusters