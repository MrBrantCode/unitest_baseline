"""
QUESTION:
Implement a function named `linear_regression` that takes four parameters: `X` (a 2D numpy array of independent variables), `y` (a 1D or 2D numpy array of dependent variables), `alpha` (a scalar learning rate), and `num_iterations` (the number of iterations for gradient descent). The function should return the optimized coefficients (including the intercept term) of the linear regression model after performing gradient descent for the specified number of iterations. 

Assume that the input arrays are not empty and that the number of rows in `X` and `y` are the same. The function should also handle the case where `y` is a 1D array and convert it to a 2D array if necessary. The learning rate and the number of iterations are assumed to be positive integers.
"""

import numpy as np

def linear_regression(X, y, alpha, num_iterations):
    """
    This function implements linear regression using gradient descent.

    Parameters:
    X (numpy array): A 2D numpy array of independent variables.
    y (numpy array): A 1D or 2D numpy array of dependent variables.
    alpha (float): The learning rate for gradient descent.
    num_iterations (int): The number of iterations for gradient descent.

    Returns:
    numpy array: The optimized coefficients (including the intercept term) of the linear regression model.
    """
    
    # Check if y is a 1D array and convert it to a 2D array if necessary
    if len(y.shape) == 1:
        y = y.reshape(-1, 1)

    # Get the number of training examples and features
    m = len(y)
    n = X.shape[1]

    # Initialize the coefficients (including the intercept term)
    theta = np.zeros((n + 1, 1))

    # Add a column of ones to X for the intercept term
    X = np.hstack((np.ones((m, 1)), X))

    # Perform gradient descent for the specified number of iterations
    for _ in range(num_iterations):
        # Compute the predicted values
        predictions = np.dot(X, theta)

        # Compute the error
        error = predictions - y

        # Compute the gradient of the cost function
        gradient = (1 / m) * np.dot(X.T, error)

        # Update the coefficients
        theta = theta - alpha * gradient

    return theta