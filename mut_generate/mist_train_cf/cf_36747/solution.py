"""
QUESTION:
Implement the `layer_norm_grad_ref` function, which calculates the gradient of the layer normalization with respect to the input `X_full`. The function should take the following parameters:
- `gout_full`: A NumPy array representing the gradient of the output of the layer normalization.
- `norm`: A NumPy array representing the normalized input (not used in this function).
- `mean_full`: A NumPy array representing the mean of the input.
- `stdev_full`: A NumPy array representing the standard deviation of the input.
- `X_full`: A NumPy array representing the original input to the layer normalization.

The function should return the gradient of the layer normalization with respect to the input `X_full`.
"""

import numpy as np
from functools import reduce
from operator import mul

def layer_norm_grad_ref(gout_full, norm, mean_full, stdev_full, X_full):
    left = reduce(mul, X_full.shape[:1], 1)
    right = reduce(mul, X_full.shape[1:], 1)
    X = np.reshape(X_full, [left, right])
    stdev = np.reshape(stdev_full, [left, 1])
    mean = np.reshape(mean_full, [left, 1])
    gout = np.reshape(gout_full, [left, right])
    dstdev_end = (-1.0) / np.power(stdev, 2.0) \
            * np.sum((X - mean) * gout, axis=1).reshape([left, 1])
    # Calculate the gradient of the layer normalization with respect to the input X_full
    dmean_end = -1.0 / stdev * np.sum(gout, axis=1).reshape([left, 1])
    dX = (1.0 / stdev) * gout + (X - mean) * dstdev_end + dmean_end
    dX_full = np.reshape(dX, X_full.shape)
    return dX_full