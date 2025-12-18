"""
QUESTION:
Implement the `gaussian_pdf` function to calculate the probability density function of a Gaussian distribution for a given x value, mean μ, and standard deviation σ using the formula: f(x; μ, σ) = (1/σ√(2π)) * e^(-(x-μ)^2 / (2σ^2)). The function should take in three arguments: x, mean, and std_dev. The result should be the probability density at the given x value.
"""

import numpy as np

def gaussian_pdf(x, mean, std_dev):
    coefficient = 1 / (std_dev * np.sqrt(2 * np.pi))
    exponent = -(np.power(x - mean, 2) / (2 * np.power(std_dev, 2)))
    return coefficient * np.exp(exponent)