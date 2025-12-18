"""
QUESTION:
Implement a `calculate_gauss_points` method in the `GaussianQuadrature` class that calculates Gaussian quadrature points and weights for a given number of points and weight function. The method should take two parameters: `numPoints` (the number of points) and `weightFunction` (a callable object that takes a single argument and returns the corresponding weights). The method should store the calculated points and normalized weights in the `_gaussPoints` dictionary, where the keys are the number of points and the values are tuples of the form `(points, weights)`.
"""

import numpy as np

def calculate_gauss_points(numPoints, weightFunction):
    """
    Calculate Gaussian quadrature points and weights for a given number of points and weight function.

    Parameters:
    numPoints (int): The number of points.
    weightFunction (callable): A callable object that takes a single argument and returns the corresponding weights.

    Returns:
    tuple: A tuple containing the calculated points and normalized weights.
    """
    rootsArray = np.polynomial.legendre.leggauss(numPoints)[0]
    weights = weightFunction(rootsArray)
    weights /= np.sum(weights)
    return rootsArray, weights