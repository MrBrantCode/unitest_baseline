"""
QUESTION:
Write a function `count_unique_submatrices(LM)` that takes a 2D array `LM` of size n x n, where elements are either 0 or 1, as input. The function should calculate the number of unique submatrices that can be formed by deleting a single row and a single column from `LM`, and then counting the number of 1s in the resulting submatrix.
"""

import numpy as np

def count_unique_submatrices(LM):
    def count(matrix):
        return np.count_nonzero(matrix == 1)

    n = LM.shape[0]
    unique_submatrices = set()

    if n > 2:
        index = np.argwhere(LM == 1)[:5]
        for it in index:
            lm_ = np.delete(LM, it[0], 0)
            lm_ = np.delete(lm_, it[1] - 1, 0)
            lm_ = np.delete(lm_, it[0], 1)
            lm = np.delete(lm_, it[1] - 1, 1)

            LM[it[0], it[1]] = 0
            LM[it[1], it[0]] = 0

            unique_submatrices.add(count(lm))

    return len(unique_submatrices)