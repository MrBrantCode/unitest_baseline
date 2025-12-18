"""
QUESTION:
Write a function `reduce_array` that takes a 3-dimensional numpy array of shape (n, m, k) as input and returns a 2-dimensional numpy array of shape (n*m, k) containing all elements from the original array. The resulting array should be sorted in ascending order based on the sum of values in each row. In case of a tie, rows should be sorted based on the first element in the row. The implementation should have a time complexity of O(n*m*k) and a space complexity of O(n*m*k).
"""

import numpy as np

def reduce_array(arr):
    n, m, k = arr.shape
    arr_2d = np.reshape(arr, (n*m, k))
    sums = np.sum(arr_2d, axis=1)
    indices = np.lexsort((arr_2d[:, 0], sums))
    return arr_2d[indices]