"""
QUESTION:
Implement a Python function `multivariate_normal_pdf` that takes in a square correlation matrix `Sigma` and a shape parameter `eta` as input, and returns the value of the probability density function (PDF) of a multivariate normal distribution, where `eta` is a positive value greater than 0 and `Sigma` is a square matrix.
"""

import numpy as np

def multivariate_normal_pdf(Sigma, eta):
    det_sigma = np.linalg.det(Sigma)
    pdf = det_sigma ** (eta - 1)
    return pdf