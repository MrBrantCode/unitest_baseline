"""
QUESTION:
Write a function `median_2d_matrix(matrix)` that determines the median value(s) of the provided 2D matrix consisting of integers. The function should return an array with two central elements if the total number of elements in the matrix is even, and just the one median if the total number of elements is odd. Assume the matrix is non-empty and all rows have the same length.
"""

import numpy as np

def median_2d_matrix(matrix):
    # flatten the 2d matrix into a 1d list
    flattened = np.array(matrix).flatten()
    flattened.sort()

    size = len(flattened)
    median = []
    
    # if size is even                
    if size % 2 == 0:
        indx = size // 2
        # get the two middle values
        median.append(flattened[indx - 1])
        median.append(flattened[indx])
    # if size is odd 
    else:
        # get the middle value
        median.append(flattened[size // 2])
        
    return median