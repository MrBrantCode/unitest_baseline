"""
QUESTION:
Write a function `flip_axis_fra(x, flipping_axis)` that takes a NumPy array `x` of shape `(n1, n2, ..., nk)` and an integer `flipping_axis` as input, and returns a new array resulting from swapping the flipping axis with the first axis, reversing the order of elements along the first axis, and then swapping the first axis back to the original flipping axis. The function should not modify the original input array.
"""

import numpy as np

def flip_axis_fra(x, flipping_axis):
    pattern = [flipping_axis]
    pattern += [el for el in range(x.ndim) if el != flipping_axis]
    inv_pattern = [pattern.index(el) for el in range(x.ndim)]

    x = np.asarray(x).swapaxes(flipping_axis, 0)  
    x = x[::-1, ...]  
    x_out = x.swapaxes(0, flipping_axis)  

    return x_out