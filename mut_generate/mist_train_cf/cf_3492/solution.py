"""
QUESTION:
Write a function `multiply_matrices(A, B)` to multiply two input matrices A and B together. 

The input matrices A and B can be of any size, where the number of rows and columns are both between 1 and 1000 (inclusive), and the number of columns in A equals the number of rows in B. 

The function should have a time complexity of O(n^3), where n is the size of the matrices, and use only basic arithmetic operations (+, *, ) and numpy's array indexing.
"""

import numpy as np

def multiply_matrices(A, B):
    m, n = A.shape[0], B.shape[1]
    result = np.zeros((m, n))

    for i in range(m):
        for j in range(n):
            result[i, j] = np.sum(A[i] * B[:, j])

    return result