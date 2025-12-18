"""
QUESTION:
Implement a function `broadcast_arrays` that takes two numpy arrays `A` and `B` as input and returns their element-wise sum, applying numpy broadcasting rules to all axes except the last two, ensuring the output has an odd number of dimensions. The function should return the resulting array `C`.
"""

import numpy as np

def broadcast_arrays(A, B):
    return A + B