"""
QUESTION:
Write a function called `compute_kl_divergence` that calculates the Kullback-Leibler divergence between two multivariate Gaussian distributions with given means and covariance matrices. The function should take four parameters: `mean1` and `cov1` for the first Gaussian distribution, and `mean2` and `cov2` for the second Gaussian distribution. Assume the second distribution is a uniform distribution for interpretation purposes, but calculate the KL divergence between the two Gaussian distributions. The function should return the computed KL divergence value.

The covariance matrix for the Gaussian distribution is given as `[[0, 1], [1, 0]]`. You can use the `numpy` and `scipy` libraries for calculations. Consider the effect of the normalization factor in the KL divergence formula and its impact on the interpretation of the result.
"""

import numpy as np

def compute_kl_divergence(mean1, cov1, mean2, cov2):
    """
    Compute Kullback–Leibler divergence between two multivariate Gaussians
    """
    # Ensure the covariance matrices are numpy arrays
    cov1, cov2 = np.array(cov1), np.array(cov2)
    
    # Calculate determinant of covariance matrices
    det_cov1, det_cov2 = np.linalg.det(cov1), np.linalg.det(cov2)
    
    # Calculate the trace of the inverse of covariance matrix 2 and covariance of 1
    trace_term = np.trace(np.dot(np.linalg.inv(cov2), cov1))
    
    # Mean difference term
    mean_diff = np.array(mean2) - np.array(mean1)
    mean_diff_term = np.dot(np.dot(mean_diff.T, np.linalg.inv(cov2)), mean_diff)
    
    # Dimensionality of the Gaussians
    k = len(mean1)
    
    # Log determinant ratio term
    log_det_ratio = np.log(det_cov2 / det_cov1)
    
    # Compute KL divergence
    kl_div = 0.5 * (trace_term + mean_diff_term - k + log_det_ratio)
    
    return kl_div