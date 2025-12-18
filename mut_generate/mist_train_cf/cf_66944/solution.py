"""
QUESTION:
Implement a function `shrink_sample_covariance_matrix` that shrinks the sample covariance matrix to make it more stable for inversion. The function should take in two parameters: `X` (a 2D array representing the data points) and `delta` (a regularization parameter). The function should return the shrunk sample covariance matrix. The input `X` is a numpy array of shape `(n, p)`, where `n` is the number of observations and `p` is the number of variables. The regularization parameter `delta` is a float value between 0 and 1.
"""

import numpy as np

def shrink_sample_covariance_matrix(X, delta):
    """
    Shrinks the sample covariance matrix to make it more stable for inversion.

    Parameters:
    X (numpy array): A 2D array representing the data points of shape (n, p).
    delta (float): A regularization parameter between 0 and 1.

    Returns:
    shrunk_cov (numpy array): The shrunk sample covariance matrix.
    """

    # Calculate the sample covariance matrix
    cov = np.cov(X.T)

    # Calculate the shrinkage target, which is the identity matrix multiplied by the average variance
    avg_var = np.mean(np.diag(cov))
    target = avg_var * np.eye(cov.shape[0])

    # Calculate the shrunk covariance matrix using the Ledoit-Wolf formula
    shrunk_cov = delta * target + (1 - delta) * cov

    return shrunk_cov