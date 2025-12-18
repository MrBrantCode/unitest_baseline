"""
QUESTION:
Create a function named `cube_root_sum` that takes a 3D matrix as input and returns a list where each element is the cube root sum of each 2D array in the 3D matrix. The function should work for a 3D list or a 3D NumPy array.
"""

import numpy as np

def entrance(matrix):
    '''Calculate the cube root sum of each 2D array in a 3D matrix'''
    
    # Initialize an empty list to save the results
    result = []

    # Iterate over each 2D array in the 3D matrix
    for twoD in matrix:
        # Calculate the sum and take the cube root
        cube_root_sum = np.cbrt(np.sum(twoD))
        # Append the cube root sum to the result list
        result.append(cube_root_sum)
    
    return result