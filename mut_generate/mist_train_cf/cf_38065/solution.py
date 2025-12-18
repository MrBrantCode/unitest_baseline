"""
QUESTION:
Create a function called `max_array_shape` that takes a list of NumPy arrays as input and returns a list representing the maximum shape in each dimension. The function should handle arrays of different dimensions and shapes.
"""

import numpy as np
from typing import List

def max_array_shape(arrays: List[np.ndarray]) -> List[int]:
    shapes = list(map(lambda x: list(x.shape), arrays))  
    ndim = len(arrays[0].shape)  
    max_shape = []

    for dim in range(ndim):
        max_dim_size = max(shape[dim] for shape in shapes)  
        max_shape.append(max_dim_size)

    return max_shape