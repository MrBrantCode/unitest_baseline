"""
QUESTION:
Write a function `markowitz_portfolio` to minimize the portfolio variance in the Markowitz portfolio theory. The function should calculate the variance of a portfolio given the weights of assets and the covariance matrix of their returns. Include the constant 1/2 in the formula for mathematical convenience when taking derivatives during optimization. Assume the input weights and covariance matrix are valid (i.e., weights sum to 1 and the covariance matrix is positive semi-definite).
"""

import numpy as np

def markowitz_portfolio(weights, covariance_matrix):
    """
    This function calculates the variance of a portfolio given the weights of assets and the covariance matrix of their returns.

    Parameters:
    weights (numpy array): Weights of assets in the portfolio.
    covariance_matrix (numpy array): Covariance matrix of the asset returns.

    Returns:
    float: The variance of the portfolio.
    """
    return 0.5 * np.dot(np.dot(weights.T, covariance_matrix), weights)