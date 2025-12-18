"""
QUESTION:
Write a function `reconstruct_initial_data` that takes in a reduced data matrix `Z`, a weight matrix `F`, and a mean matrix `mean_matrix` as input, and returns the reconstructed initial data using the first ten principal components. Assume that `Z` is the result of applying PCA with `n_components=10`. The reconstructed initial data should be calculated using the formula `Z*F+mean_matrix`. If the PCA object cannot be trained due to lack of initial data, the function should simply use `Z` directly in the calculation.
"""

import numpy as np

def reconstruct_initial_data(Z, F, mean_matrix):
    """
    Reconstructs the initial data using the first ten principal components.

    Args:
        Z (numpy array): Reduced data matrix.
        F (numpy array): Weight matrix.
        mean_matrix (numpy array): Mean matrix.

    Returns:
        numpy array: Reconstructed initial data.
    """
    # Check if PCA object can be trained
    # Since we can't know this from the given data, we assume it can't be trained
    # and use Z directly in the calculation
    reconstructed_data = np.matmul(Z, F.T) + mean_matrix
    return reconstructed_data