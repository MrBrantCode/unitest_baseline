"""
QUESTION:
Write a function named `logistic_spline_probability` that calculates the probability of the dependent variable in a spline binary logistic regression model. The function should take in the coefficients of the regression model (`b0`, `b1`, ..., `bn`) and the spline value (`X`) as inputs. The function should return the calculated probability `P(1)`.
"""

import math

def logistic_spline_probability(b, X):
    """
    Calculate the probability of the dependent variable in a spline binary logistic regression model.

    Parameters:
    b (list): coefficients of the regression model (b0, b1, ..., bn)
    X (list): spline values corresponding to each coefficient

    Returns:
    float: the calculated probability P(1)
    """
    Y = sum([i*j for i, j in zip(b, X)])  # calculate Y' using the regression model
    probability = math.exp(Y) / (1 + math.exp(Y))  # calculate P(1) using the logistic function
    return probability