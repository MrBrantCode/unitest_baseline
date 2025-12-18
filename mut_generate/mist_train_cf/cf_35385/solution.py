"""
QUESTION:
Implement a function `gaussian_quadrature_hermite(f, n)` that calculates the approximate integral of a given callable function `f` over the entire real line using Gaussian quadrature with `n` nodes and weights based on the Hermite polynomials. The function should take a callable `f` and an integer `n` as input and return the approximate integral. The Gaussian quadrature formula should be approximated as the sum of the products of the weights and the function values at the nodes.
"""

import numpy as np
import numpy.polynomial.hermite as herm

def gaussian_quadrature_hermite(f, n):
    nodes, weights = herm.hermgauss(n)  
    integral = np.sum(weights * f(nodes))  
    return integral