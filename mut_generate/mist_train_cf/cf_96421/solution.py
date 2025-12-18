"""
QUESTION:
Compute the sum of all elements in a 2D numpy array with at least 2 rows and 3 columns, excluding elements that are divisible by 2 and greater than 10, given that the array contains only positive integers.
"""

import numpy as np

def sum_of_elements(arr):
    filtered_arr = arr[(arr % 2 != 0) | (arr <= 10)]
    return np.sum(filtered_arr)