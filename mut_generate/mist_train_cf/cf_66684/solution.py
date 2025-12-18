"""
QUESTION:
Write a function `pca_svd_equivalence` that performs the steps necessary to achieve the same projection as Singular Value Decomposition (SVD) in the context of Principal Component Analysis (PCA). The function should take a dataset as input and return the transformed dataset with the same projection as SVD. The function should follow these steps: standardize the dataset, compute the covariance matrix, compute eigenvectors and eigenvalues, sort eigenvalues in decreasing order, choose the top k eigenvectors, form the projection matrix, and transform the original dataset. Assume that the input dataset is a 2D array and k is the desired dimensionality of the output dataset.
"""

import numpy as np

def pca_svd_equivalence(dataset, k):
    """
    This function performs the steps necessary to achieve the same projection as 
    Singular Value Decomposition (SVD) in the context of Principal Component Analysis (PCA).

    Parameters:
    dataset (2D array): The input dataset.
    k (int): The desired dimensionality of the output dataset.

    Returns:
    transformed_dataset (2D array): The transformed dataset with the same projection as SVD.
    """
    
    # Standardize the dataset
    standardized_dataset = (dataset - np.mean(dataset, axis=0)) / np.std(dataset, axis=0)
    
    # Compute the covariance matrix
    covariance_matrix = np.cov(standardized_dataset.T)
    
    # Compute Eigenvectors and Eigenvalues
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
    
    # Sort eigenvalues in decreasing order and choose the top k eigenvectors
    idx = eigenvalues.argsort()[::-1]
    top_k_eigenvectors = eigenvectors[:, idx[:k]]
    
    # Form the projection matrix
    projection_matrix = top_k_eigenvectors
    
    # Transform the original dataset
    transformed_dataset = standardized_dataset @ projection_matrix
    
    return transformed_dataset