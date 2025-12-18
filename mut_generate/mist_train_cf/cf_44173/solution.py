"""
QUESTION:
Identify the distribution given the probability density function (pdf) f(x) = (1 / sqrt(2 * pi * x^3)) * exp(-0.5 * ((x - mu) / (mu * sqrt(x)))^2).
"""

import math

def modified_gaussian(x, mu):
    """
    Modified Gaussian distribution probability density function (pdf).
    
    Parameters:
    x (float): The point at which to evaluate the pdf.
    mu (float): The mean of the distribution.
    
    Returns:
    float: The value of the pdf at x.
    """
    return (1 / math.sqrt(2 * math.pi * x**3)) * math.exp(-0.5 * ((x - mu) / (mu * math.sqrt(x)))**2)