"""
QUESTION:
Implement the function `custom_kernel` that takes two input vectors `x` and `x'` and returns the value of a custom kernel function k(x, x') that combines the properties of the Matern32 and Matern52 kernels. The Matern32 kernel is defined as k(x, x') = (1 + sqrt(3)*r)*exp(-sqrt(3)*r) and the Matern52 kernel is defined as k(x, x') = (1 + sqrt(5)*r + 5/3*r^2)*exp(-sqrt(5)*r), where r is the Euclidean distance between x and x'. The function should also take into account optional parameters `l` (lengthscale) and `sigma` (mixture parameter) to allow for flexibility in modeling complex relationships in the data.
"""

import numpy as np

def custom_kernel(x, x_prime, l=1.0, sigma=1.0):
    # Calculate the Euclidean distance
    r = np.linalg.norm(x - x_prime)

    # Define the Matern32 and Matern52 kernel functions
    matern32 = (1 + np.sqrt(3)*r/l)*np.exp(-np.sqrt(3)*r/l)
    matern52 = (1 + np.sqrt(5)*r/l + 5/3*(r/l)**2)*np.exp(-np.sqrt(5)*r/l)

    # Combine the two kernel functions using a weighted sum
    combined_kernel = (1 - sigma)*matern32 + sigma*matern52

    return combined_kernel