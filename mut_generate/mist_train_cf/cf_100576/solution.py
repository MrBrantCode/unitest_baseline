"""
QUESTION:
Create a function `mahalanobis_distance` that calculates the Mahalanobis distance between two multivariate points `point1` and `point2` with a given covariance matrix `cov_matrix`. The function should return the Mahalanobis distance as a float. The covariance matrix is a square matrix of the same dimension as the points, representing the variance and covariance between variables.
"""

import numpy as np

def mahalanobis_distance(point1, point2, cov_matrix):
    """
    Calculate the Mahalanobis distance between two multivariate points.

    Parameters:
    point1 (numpy array): The first multivariate point.
    point2 (numpy array): The second multivariate point.
    cov_matrix (numpy array): The covariance matrix of the dataset.

    Returns:
    float: The Mahalanobis distance between the two points.
    """
    inv_cov_matrix = np.linalg.inv(cov_matrix)
    diff = point1 - point2
    mahal_dist = np.sqrt(np.dot(np.dot(diff, inv_cov_matrix), diff.T))
    return mahal_dist