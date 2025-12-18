"""
QUESTION:
Create a function called `calculate_correlation_coefficient` that takes two lists of numbers `X` and `Y` as input and calculates the correlation coefficient between them. The function should also calculate and return the standard deviations of `X` and `Y`. Assume that the input lists are not empty and have the same length.
"""

import math

def calculate_correlation_coefficient(X, Y):
    # Calculate the mean of X and Y
    mean_X = sum(X) / len(X)
    mean_Y = sum(Y) / len(Y)

    # Calculate the standard deviation of X and Y
    std_X = math.sqrt(sum([(x - mean_X) ** 2 for x in X]) / (len(X) - 1))
    std_Y = math.sqrt(sum([(y - mean_Y) ** 2 for y in Y]) / (len(Y) - 1))

    # Calculate the correlation coefficient
    corr_coef = sum([(x - mean_X) * (y - mean_Y) for x, y in zip(X, Y)]) / ((len(X) - 1) * std_X * std_Y)

    return corr_coef, std_X, std_Y