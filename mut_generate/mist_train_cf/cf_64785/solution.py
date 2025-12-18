"""
QUESTION:
Write a function named `invert_elements` that takes a multidimensional integer array as input and returns the array with the elements of each sub-array reversed, while maintaining the original ordering and structure of the broader multidimensional array. The function should work for arrays of any size and dimension, with no restrictions on the number of sub-arrays or elements within each sub-array.
"""

def invert_elements(arr):
    return [x[::-1] for x in arr]