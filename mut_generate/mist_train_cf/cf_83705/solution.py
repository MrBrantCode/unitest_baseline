"""
QUESTION:
Create a function named `dot_product` that calculates the dot product of two 1D arrays. The function should handle arrays of different lengths by filling the missing elements with 1. The dot product is calculated as the sum of the products of corresponding elements in the two arrays, where each element in the first array is multiplied by the corresponding element in the second array.
"""

import itertools

def dot_product(array1, array2):
    dp = 0
    for a, b in itertools.zip_longest(array1, array2, fillvalue=1):
        dp += a * b
    return dp