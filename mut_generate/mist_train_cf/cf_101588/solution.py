"""
QUESTION:
Implement a function `gaussian_pdf` that calculates the probability density function of a Gaussian distribution for a given x value with a mean μ and standard deviation σ. The function should take in x, μ, and σ as arguments and return the probability density. The probability density function should be calculated using the formula f(x; μ, σ) = (1/σ√(2π)) * e^(-(x-μ)^2 / (2σ^2)).
"""

import numpy as np

def gaussian_pdf(x, mean, std_dev):
    coefficient = 1 / (std_dev * np.sqrt(2 * np.pi))
    exponent = -(np.power(x - mean, 2) / (2 * np.power(std_dev, 2)))
    return coefficient * np.exp(exponent)