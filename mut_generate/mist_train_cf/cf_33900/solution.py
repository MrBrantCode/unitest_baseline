"""
QUESTION:
Implement the function `find_squares_opt(array)` that takes a list of integers as input and returns a new list containing the squares of each integer incremented by 1. The input list can have up to 10^5 elements, and each integer is within the range -10^9 to 10^9.
"""

import numpy as np

def find_squares_opt(array):
    arr = np.array(array)  
    return list(arr**2 + 1) 