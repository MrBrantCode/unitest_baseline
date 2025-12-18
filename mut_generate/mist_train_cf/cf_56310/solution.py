"""
QUESTION:
Create a function `prod_signs` that takes an array of numbers as input and returns the sign of the product of all unique, non-zero floating point numbers in the array. The function should discard any duplicate and zero values, as well as non-floating point numbers. The output should be 1.0 for a positive product and -1.0 for a negative product.
"""

import numpy as np
import math

def prod_signs(arr):
    # Filter arr to include only unique, nonzero, floating point numbers
    arr = set(x for x in arr if isinstance(x, float) and x != 0.0)
    # Use numpy prod to get the product of all numbers in the filtered list
    product = np.prod(list(arr))
    # Return the sign of the product
    return math.copysign(1, product)