"""
QUESTION:
Write a function `gaussian_pdf(x, mean, std_dev)` that calculates the probability density function of a Gaussian distribution given the value `x`, mean `mean`, and standard deviation `std_dev` using the formula: f(x; μ, σ) = (1/σ√(2π)) * e^(-(x-μ)^2 / (2σ^2)). The function should return the calculated probability density. The input values `x`, `mean`, and `std_dev` are numbers, and `std_dev` is non-zero.
"""

import numpy as np
def gaussian_pdf(x, mean, std_dev):
    coefficient = 1 / (std_dev * np.sqrt(2 * np.pi))
    exponent = -(np.power(x - mean, 2) / (2 * np.power(std_dev, 2)))
    return coefficient * np.exp(exponent)