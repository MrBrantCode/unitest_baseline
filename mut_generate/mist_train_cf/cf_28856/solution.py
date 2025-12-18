"""
QUESTION:
Implement a function `calculate_matrix_exponential` that calculates the matrix exponential of a given square covariance matrix A, where the matrix exponential is defined as expm(A) = V * exp(Λ) * V^T. Here, V is the matrix of eigenvectors of A and Λ is the diagonal matrix of eigenvalues of A. The function should take a covariance matrix as input and return the matrix exponential.
"""

import numpy

def calculate_matrix_exponential(Ci):
    """
    Calculate the matrix exponential of a given covariance matrix.

    :param Ci: the covariance matrix
    :returns: the matrix exponential
    """
    eigenvalues, eigenvectors = numpy.linalg.eig(Ci)  # Calculate eigenvalues and eigenvectors
    exp_lambda = numpy.diag(numpy.exp(eigenvalues))  # Create the diagonal matrix of exponential eigenvalues
    matrix_exponential = numpy.dot(numpy.dot(eigenvectors, exp_lambda), numpy.transpose(eigenvectors))  # Calculate the matrix exponential
    return matrix_exponential