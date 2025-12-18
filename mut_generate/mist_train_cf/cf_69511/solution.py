"""
QUESTION:
Write a function `find_max_sum` that takes a 3D numpy array `arr` as input and returns the maximum sum of any subarray within `arr`. The function should work for arrays of any size, but for the purposes of this problem, assume the input array is a 4x4x4 cube of random floating-point numbers between -1 and 1. The function should handle the case where the input array contains all negative numbers.
"""

import numpy as np

def find_max_sum(arr):
    max_sum = -np.inf
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            for k in range(arr.shape[2]):
                for x in range(i, arr.shape[0]):
                    for y in range(j, arr.shape[1]):
                        for z in range(k, arr.shape[2]):
                            subarray = arr[i:x+1, j:y+1, k:z+1]
                            curr_sum = np.sum(subarray)
                            max_sum = max(max_sum, curr_sum)
    return max_sum