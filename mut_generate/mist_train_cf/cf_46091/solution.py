"""
QUESTION:
Write a function `to_binary_matrix` that takes an array of integers `a` and an integer `m` as input, and returns a 2D numpy array where each row represents the binary representation of the corresponding integer in `a`, padded to a length of `m`. The function should work for both positive and negative integers, and should be able to handle integer overflow.
"""

import numpy as np

def to_binary_matrix(a, m):
    return np.array([[i>>d & 1 for d in range(m-1, -1, -1)] for i in a])