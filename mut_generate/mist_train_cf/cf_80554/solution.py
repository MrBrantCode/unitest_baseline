"""
QUESTION:
Write a function `product(arr)` that computes the product of all integers in a given multidimensional array `arr`, where the array can be up to three dimensions. Assume the input array is not empty and contains no empty sub-arrays.
"""

def product(arr):
    output = 1
    for i in arr:
        if isinstance(i, list):
            output *= product(i)
        else:
            output *= i
    return output