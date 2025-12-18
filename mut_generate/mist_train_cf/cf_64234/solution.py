"""
QUESTION:
Implement a function called `clustering_technique` to identify an algorithm recognized as a clustering technique in machine learning theory.
"""

def clustering_technique(algorithm):
    clustering_algorithms = ["K-Means", "Hierarchical Clustering", "DBSCAN", "Gaussian Mixture Models"]
    return algorithm in clustering_algorithms