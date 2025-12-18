"""
QUESTION:
Create a function named `max_matrix_sum` that takes a 3D numpy array as input, where the array contains multiple 2D matrices of the same size. The function should calculate the sum of elements in each matrix and return the maximum sum of all matrices. The input 3D array has a shape of (n, 3, 2), where n is the number of matrices, and each matrix has a size of 3x2.
"""

import numpy as np

# Function to calculate the sum of each matrix and return the maximum sum
def max_matrix_sum(array):
    sums = [np.sum(array[i]) for i in range(array.shape[0])]
    return max(sums)