"""
QUESTION:
Given a payoff matrix A and a price vector p, calculate the state price vector q, where q = A^-1 * p. The payoff matrix A is a 3x3 matrix with the following values:

[[1, 0.9, 0.8],
[1, 1.1, 1.2],
[1, 1.2, 1.1]]

and the price vector p is [1, 1.05, 1.03]. The state price vector q should be calculated using matrix inversion and multiplication.
"""

import numpy as np

def state_price_vector(payoff_matrix, price_vector):
    """
    Calculate the state price vector q, where q = A^-1 * p.

    Parameters:
    payoff_matrix (numpy array): A 3x3 payoff matrix.
    price_vector (numpy array): A 1x3 price vector.

    Returns:
    numpy array: The state price vector q.
    """
    # Calculate the inverse of the payoff matrix
    inverse_payoff_matrix = np.linalg.inv(payoff_matrix)
    
    # Multiply the inverse payoff matrix by the price vector to get the state price vector
    state_price_vector = np.dot(inverse_payoff_matrix, price_vector)
    
    return state_price_vector