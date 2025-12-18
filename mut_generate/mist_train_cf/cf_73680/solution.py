"""
QUESTION:
Write a function `geometric_mean(array)` that calculates the geometric mean of the elements in the given array. The function should return the geometric mean if all elements in the array are non-negative, and an error message if the array contains a negative number. The geometric mean of 'n' numbers is the 'n'-th root of the product of the numbers.
"""

import math
import numpy as np

def geometric_mean(array):
    if all(i >= 0 for i in array):
        product = np.prod(array)
        gm = math.pow(product, 1/len(array))
        return gm
    else:
        return "Error: Negative numbers not allowed for geometric mean calculation."