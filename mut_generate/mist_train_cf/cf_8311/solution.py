"""
QUESTION:
Create a function `find_first_non_repeating(arr)` that finds the index of the first non-repeating element in a given numpy array `arr` containing only positive integers. If there are no non-repeating elements, the function should return -1. The size of the array will not exceed 10^5 elements.
"""

import numpy as np

def find_first_non_repeating(arr):
    unique, counts = np.unique(arr, return_counts=True)  
    non_repeating = unique[counts == 1]  
    if len(non_repeating) == 0:  
        return -1
    else:
        first_non_repeating_index = np.where(arr == non_repeating[0])[0][0]  
        return first_non_repeating_index