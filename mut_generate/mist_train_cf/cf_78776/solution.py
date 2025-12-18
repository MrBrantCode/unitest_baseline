"""
QUESTION:
Create a function named `replace_7s` that takes a 2D numpy array as input and returns the modified array and the count of -1s. The function should replace all numbers in the array which are divisible by 7 or contain the digit 7 with -1. The function should be able to handle numerical 2D arrays of different sizes.
"""

import numpy as np

def replace_7s(arr):
    """Replace all numbers in the 2D array which are divisible by 7 or contain the digit 7 with -1"""
    # create a vectorized function that checks for divisibility by 7 or containing 7, and returns -1 if so
    func = np.vectorize(lambda x: -1 if (x % 7 == 0) or '7' in str(x) else x)
    # apply the function to the array
    updated_arr = func(arr)
    # count the number of -1s
    count_neg1 = np.count_nonzero(updated_arr == -1)
    return updated_arr, count_neg1