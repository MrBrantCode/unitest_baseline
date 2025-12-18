"""
QUESTION:
Implement a function `gaussian_pdf` to calculate the probability density function of a Gaussian distribution. The function should take three parameters: `x`, the value at which to calculate the probability density, `mean`, the average value of the distribution, and `std_dev`, the standard deviation of the distribution. The function should use the formula `f(x; μ, σ) = (1/σ√(2π)) * e^(-(x-μ)^2 / (2σ^2))`. The function should return the calculated probability density.
"""

import numpy as np

def gaussian_pdf(x, mean, std_dev):
    coefficient = 1 / (std_dev * np.sqrt(2 * np.pi))
    exponent = -(np.power(x - mean, 2) / (2 * np.power(std_dev, 2)))
    return coefficient * np.exp(exponent)