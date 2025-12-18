"""
QUESTION:
Write a function called `calculate_correlation` that takes two lists of numbers `X` and `Y` as input and returns the standard deviations of `X` and `Y` and their correlation coefficient. The function should calculate the mean, standard deviation, and correlation coefficient using the sample standard deviation formula. Assume that the input lists are not empty and have the same length.
"""

import math

def calculate_correlation(X, Y):
    """
    Calculate the standard deviations of X and Y and their correlation coefficient.

    Args:
    X (list): A list of numbers.
    Y (list): A list of numbers.

    Returns:
    tuple: A tuple containing the standard deviation of X, the standard deviation of Y, and their correlation coefficient.
    """
    # Calculate the mean of X and Y
    mean_X = sum(X) / len(X)
    mean_Y = sum(Y) / len(Y)

    # Calculate the standard deviation of X and Y
    std_X = math.sqrt(sum([(x - mean_X) ** 2 for x in X]) / (len(X) - 1))
    std_Y = math.sqrt(sum([(y - mean_Y) ** 2 for y in Y]) / (len(Y) - 1))

    # Calculate the correlation coefficient
    corr_coef = sum([(x - mean_X) * (y - mean_Y) for x, y in zip(X, Y)]) / ((len(X) - 1) * std_X * std_Y)

    return std_X, std_Y, corr_coef