"""
QUESTION:
Implement a function called `perform_pca` that takes a dataset `X` and the number of principal components `k` as input, and returns the principal components of `X` after performing Principal Component Analysis (PCA). The implementation should not use any built-in functions or libraries for matrix operations.
"""

import numpy as np

def perform_pca(X, k):
    """
    Perform PCA on the dataset X and return the principal components.
    k: Number of principal components to keep.
    """
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    standardized_X = (X - mean) / std

    n = X.shape[0]
    covariance_matrix = np.dot(standardized_X.T, standardized_X) / (n-1)

    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]

    principal_components = sorted_eigenvectors[:, :k]

    projected_X = np.dot(standardized_X, principal_components)

    return projected_X