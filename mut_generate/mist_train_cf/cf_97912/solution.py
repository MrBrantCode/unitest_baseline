"""
QUESTION:
Implement a function called `array_operations` that takes in a 2D numpy array and performs the following operations: 
- prints the shape of the array
- reshapes the array into a 1D array
- splits the 1D array into two equal parts along the first axis
- flattens the original 2D array into a 1D array
- concatenates the two split parts along the first axis to form the original 1D array.

The function should return the concatenated 1D array. The input array can be any 2D numpy array, and the function should work for arrays of any size.
"""

import numpy as np

def array_operations(arr):
    print(arr.shape)
    one_d_array = arr.reshape((arr.size,))
    split_index = one_d_array.shape[0] // 2
    split_part1, split_part2 = np.split(one_d_array, [split_index])
    flattened_array = arr.flatten()
    concatenated_array = np.concatenate((split_part1, split_part2))
    return concatenated_array