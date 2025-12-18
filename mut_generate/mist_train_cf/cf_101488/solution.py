"""
QUESTION:
Write a function `calculate_correlation` that calculates the standard deviation of two input lists `X` and `Y` and uses those values to calculate the correlation coefficient between `X` and `Y`. The function should return the standard deviation of `X`, the standard deviation of `Y`, and the correlation coefficient.
"""

import math

def calculate_correlation(X, Y):
    # Calculate the mean of X and Y
    mean_X = sum(X) / len(X)
    mean_Y = sum(Y) / len(Y)
    
    # Calculate the standard deviation of X and Y
    std_X = math.sqrt(sum([(x - mean_X) ** 2 for x in X]) / (len(X) - 1))
    std_Y = math.sqrt(sum([(y - mean_Y) ** 2 for y in Y]) / (len(Y) - 1))
    
    # Calculate the correlation coefficient
    corr_coef = sum([(x - mean_X) * (y - mean_Y) for x, y in zip(X, Y)]) / ((len(X) - 1) * std_X * std_Y)
    
    return std_X, std_Y, corr_coef