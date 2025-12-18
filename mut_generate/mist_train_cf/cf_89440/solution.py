"""
QUESTION:
Write a function `sum_of_array` that takes a 2D numpy array as input, with a minimum of 3 rows and 4 columns, containing only positive integers. The function should calculate the sum of all elements that are not divisible by 3 and not greater than 10. The time complexity of the solution should be O(n), where n is the total number of elements in the array.
"""

import numpy as np

def sum_of_array(arr):
    mask = np.logical_and(arr % 3 != 0, arr <= 10)
    return np.sum(arr[mask])