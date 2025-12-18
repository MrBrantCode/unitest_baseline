"""
QUESTION:
Design a function named `analyze_dataset` to implement a regression model algorithm that can be used to analyze a given dataset. The function should be able to handle various types of data and analysis requirements.
"""

import numpy as np

def analyze_dataset(X, y):
    """
    This function implements a simple linear regression model to analyze a given dataset.

    Parameters:
    X (list): Independent variable(s) of the dataset.
    y (list): Dependent variable of the dataset.

    Returns:
    tuple: A tuple containing the coefficient and intercept of the regression line.
    """

    # Convert the input lists to numpy arrays
    X = np.array(X)
    y = np.array(y)

    # Calculate the mean of X and y
    mean_x = np.mean(X)
    mean_y = np.mean(y)

    # Calculate the deviations from the mean for X and y
    dev_x = X - mean_x
    dev_y = y - mean_y

    # Calculate the slope (coefficient) of the regression line
    coefficient = np.sum(dev_x * dev_y) / np.sum(dev_x ** 2)

    # Calculate the intercept of the regression line
    intercept = mean_y - coefficient * mean_x

    return coefficient, intercept