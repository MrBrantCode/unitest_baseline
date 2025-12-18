"""
QUESTION:
Create a function called 'linear_regression_sgd' that implements linear regression using Stochastic Gradient Descent (SGD) in Python. The function should accept a 2D array of features (X), a 1D array of targets (y), the learning rate, and the number of iterations as parameters. The function should return the coefficients (weights) of the linear regression model. 

Restrictions: The function should not use any pre-built linear regression or SGD functions from libraries like scikit-learn.
"""

def linear_regression_sgd(X, y, learning_rate, iterations):
    """
    This function implements linear regression using Stochastic Gradient Descent (SGD).

    Parameters:
    X (2D array): Features
    y (1D array): Targets
    learning_rate (float): Learning rate for SGD
    iterations (int): Number of iterations

    Returns:
    coefficients (list): Coefficients (weights) of the linear regression model
    """

    # Initialize coefficients (weights) with zeros
    coefficients = [0.0] * (len(X[0]) + 1)

    # Add a column of ones to X for the bias term
    X = [[1.0] + row for row in X]

    # Perform SGD for the specified number of iterations
    for _ in range(iterations):
        for i, row in enumerate(X):
            # Calculate the predicted value using current coefficients
            predicted = sum([coefficients[j] * row[j] for j in range(len(row))])

            # Calculate the error
            error = predicted - y[i]

            # Update coefficients using the error and learning rate
            for j in range(len(row)):
                coefficients[j] -= learning_rate * error * row[j]

    return coefficients