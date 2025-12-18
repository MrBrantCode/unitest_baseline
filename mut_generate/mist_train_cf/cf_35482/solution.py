"""
QUESTION:
Implement a function `reduce_vector(vectors, reduction_vector)` that takes a 2D numpy array `vectors` and a 1D numpy array `reduction_vector` as input. The function should return a 2D numpy array where each row contains the result of element-wise subtracting the `reduction_vector` from the corresponding vector in `vectors`. Assume that the dimensions of the input arrays are compatible for the reduction operation.
"""

import numpy as np

def reduce_vector(vectors, reduction_vector):
    return vectors - reduction_vector