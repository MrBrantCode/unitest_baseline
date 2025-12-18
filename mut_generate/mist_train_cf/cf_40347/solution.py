"""
QUESTION:
Implement a function `calculate_mse(inputs, outputs)` that calculates the mean squared error (MSE) between two given NumPy arrays `inputs` and `outputs`. The function should return the mean of the squared differences between corresponding elements in the two arrays. Assume that `inputs` and `outputs` have the same length.
"""

import numpy as np

def calculate_mse(inputs, outputs):
    mse = np.mean((inputs - outputs) ** 2)
    return mse