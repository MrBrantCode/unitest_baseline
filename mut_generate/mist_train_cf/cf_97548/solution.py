"""
QUESTION:
Implement a function `gaussian_pdf` to calculate the probability density function of a Gaussian distribution given the mean `μ` (mean) and standard deviation `σ` (std_dev) for a given value `x`. The formula to use is `f(x; μ, σ) = (1/σ√(2π)) * e^(-(x-μ)^2 / (2σ^2))`.
"""

import numpy as np

def gaussian_pdf(x, mean, std_dev):
    """
    Calculate the probability density function of a Gaussian distribution.

    Parameters:
    x (float): The value at which to calculate the probability density.
    mean (float): The mean of the Gaussian distribution.
    std_dev (float): The standard deviation of the Gaussian distribution.

    Returns:
    float: The probability density of the Gaussian distribution at x.
    """
    coefficient = 1 / (std_dev * np.sqrt(2 * np.pi))
    exponent = -(np.power(x - mean, 2) / (2 * np.power(std_dev, 2)))
    return coefficient * np.exp(exponent)