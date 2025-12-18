"""
QUESTION:
Implement a function named `matrix_multiplication` that takes two input matrices `A` and `B` and returns their product. The function should be able to handle matrices of any size where the number of rows and columns are between 1 and 1000 (inclusive), with a time complexity of O(n^3). The function must use only basic arithmetic operations and numpy's array indexing, without utilizing any built-in functions for matrix multiplication or loops/recursion.
"""

import numpy as np

def entance(A, B):
    return np.sum(A[:, np.newaxis] * B, axis=2)