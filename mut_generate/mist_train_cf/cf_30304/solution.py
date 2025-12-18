"""
QUESTION:
Implement a function `multi_dim_slice(m, slices, axis)` that performs slicing on a multi-dimensional NumPy array `m` along a specified axis. The `slices` parameter should be applied to the specified `axis`, while the other axes should be left unchanged. The function should return the sliced array. Assume that the input array `m` and the input slices will always be valid for the given array dimensions.
"""

import numpy as np

def multi_dim_slice(m, slices, axis):
    sl = [slice(None)] * m.ndim
    sl[axis] = slices
    return m[tuple(sl)]