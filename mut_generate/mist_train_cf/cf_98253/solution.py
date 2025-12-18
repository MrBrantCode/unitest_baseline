"""
QUESTION:
Write a function `mahalanobis_distance` that calculates the Mahalanobis distance between two points in a multivariate dataset. The function should take as input three parameters: `point1` and `point2`, the two multivariate points, and `cov_matrix`, the covariance matrix of the dataset. The function should return the Mahalanobis distance between the two points.
"""

import numpy as np

def mahalanobis_distance(point1, point2, cov_matrix):
    """
    Calculate the Mahalanobis distance between two points in a multivariate dataset.

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