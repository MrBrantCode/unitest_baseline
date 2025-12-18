"""
QUESTION:
Implement a function `gaussian_pdf(x, mean, std_dev)` that calculates the probability density function of a Gaussian distribution with mean `μ` (mean) and standard deviation `σ` (std_dev) for a given x value using the formula `f(x; μ, σ) = (1/σ√(2π)) * e^(-(x-μ)^2 / (2σ^2))`. The function should take in `x`, `mean`, and `std_dev` as arguments and return the probability density.
"""

import numpy as np

def gaussian_pdf(x, mean, std_dev):
    coefficient = 1 / (std_dev * np.sqrt(2 * np.pi))
    exponent = -(np.power(x - mean, 2) / (2 * np.power(std_dev, 2)))
    return coefficient * np.exp(exponent)