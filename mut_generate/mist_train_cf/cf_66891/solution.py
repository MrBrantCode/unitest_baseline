"""
QUESTION:
Write a function called `poisson_gamma_mixture_expected_value` that takes two parameters `alpha` and `beta` representing the shape and rate parameters of a gamma distribution respectively. The function should return the expected value of a Poisson-Gamma mixture distribution, given that the Poisson distribution's parameter λ follows a Gamma distribution with parameters `alpha` and `beta`. The function should not take any other parameters.
"""

import math

def poisson_gamma_mixture_expected_value(alpha, beta):
    """
    Calculate the expected value of a Poisson-Gamma mixture distribution.

    Parameters:
    alpha (float): The shape parameter of the gamma distribution.
    beta (float): The rate parameter of the gamma distribution.

    Returns:
    float: The expected value of the Poisson-Gamma mixture distribution.
    """
    return alpha / beta