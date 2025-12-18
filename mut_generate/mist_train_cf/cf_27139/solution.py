"""
QUESTION:
Implement a function `weighted_sum_with_sigmoid` that calculates the weighted sum of a given set of values using a sigmoid function as the weighting factor. The sigmoid function is defined as `0.5 * (tanh(1.5 * pi * (x - 0.5)) + 1)`. The function takes two NumPy arrays `Y` and `T` as input, where `Y` has shape `(n, m)` and `T` has shape `(n,)`. The function should return a NumPy array of shape `(m,)` containing the weighted sum of the values in `Y` using the sigmoid function as the weighting factor for each time step.
"""

import numpy as np

def weighted_sum_with_sigmoid(Y: np.ndarray, T: np.ndarray) -> np.ndarray:
    sigmoid = 0.5 * (np.tanh(1.5 * np.pi * (T - 0.5)) + 1.0)
    weighted_sum = np.sum(Y * sigmoid[:, np.newaxis], axis=0)
    return weighted_sum