"""
QUESTION:
Calculate the Kronecker product of n matrices using the NumPy package. The function `kronecker_product` should take a list of 2D NumPy arrays as input and return the Kronecker product of all matrices in the list. The function should be optimized for efficiency and should not require unnecessary computation or storage.
"""

import numpy as np

def kronecker_product(matrices):
    result = matrices[0]
    for matrix in matrices[1:]:
        result = np.kron(result, matrix)
    return result