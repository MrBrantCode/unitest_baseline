"""
QUESTION:
Write a function `calculate_u` that calculates the factor `u` in the Cox, Ross, & Rubinstein (CRR) model given the annualized standard deviation of the asset's return `sigma`, the number of periods `n`, and the time period `t`. The function should return the calculated value of `u`. Assume that the asset price follows a lognormal distribution. 

The function should be able to handle any valid input values of `sigma`, `n`, and `t` where `sigma` is a positive number and `n` and `t` are positive integers.
"""

import math

def calculate_u(sigma, n, t):
    """
    Calculate the factor u in the Cox, Ross, & Rubinstein (CRR) model.

    Parameters:
    sigma (float): Annualized standard deviation of the asset's return.
    n (int): Number of periods.
    t (int): Time period.

    Returns:
    float: The calculated value of u.
    """
    return math.exp(sigma * math.sqrt(n / t))