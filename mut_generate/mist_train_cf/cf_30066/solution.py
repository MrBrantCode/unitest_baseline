"""
QUESTION:
Implement two methods, `compute_distances` and `regularize_cost`, for a class `CostComputation` with an instance variable `lambdaRate` that represents the regularization rate.

1. `compute_distances(theta, y)`: This method takes in the model parameters `theta` and actual values `y` as input and returns the distances between the model's predictions and the actual values.

2. `regularize_cost(cost, theta)`: This method takes in the cost and model parameters `theta` as input and returns the regularized cost if `lambdaRate` is greater than 0.0.

Restrictions:
- The `lambdaRate` is used to determine whether regularization is applied.
- The regularization term is calculated as `(lambdaRate / (2 * m)) * np.sum(np.power(theta, 2))`, where `m` is the number of data points.
- If `lambdaRate` is not greater than 0.0, the cost remains unchanged.
"""

import numpy as np

def compute_distances(theta, y):
    """
    Compute the distances between model predictions and actual values.

    Args:
    theta (numpy array): Model parameters.
    y (numpy array): Actual values.

    Returns:
    numpy array: Distances between model predictions and actual values.
    """
    distances = np.abs(np.subtract(theta, y))
    return distances

def regularize_cost(cost, theta, lambdaRate, m):
    """
    Apply regularization to the cost if lambdaRate is greater than 0.0.

    Args:
    cost (float): Cost to be regularized.
    theta (numpy array): Model parameters.
    lambdaRate (float): Regularization rate.
    m (int): Number of data points.

    Returns:
    float: Regularized cost if lambdaRate > 0.0, otherwise the original cost.
    """
    if lambdaRate > 0.0:
        regularization_term = (lambdaRate / (2 * m)) * np.sum(np.power(theta, 2))
        regularized_cost = cost + regularization_term
        return regularized_cost
    else:
        return cost