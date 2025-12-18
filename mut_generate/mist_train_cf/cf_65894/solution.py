"""
QUESTION:
Write a function `european_option_upper_bound` to find the upper bound of a European option E1, given the stock price S, exercise price X, risk-free rate r, and time to maturity T. The function should take these parameters as inputs and return the upper bound for E1. Assume that the inputs are all non-negative and that T is in years.
"""

import math

def european_option_upper_bound(S, X, r, T):
    """
    This function calculates the upper bound of a European option E1.

    Parameters:
    S (float): The stock price.
    X (float): The exercise price.
    r (float): The risk-free rate.
    T (float): The time to maturity in years.

    Returns:
    float: The upper bound for E1.
    """
    upper_bound = 2 * S - X * math.exp(-r * T)
    return upper_bound