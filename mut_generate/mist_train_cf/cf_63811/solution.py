"""
QUESTION:
Write a function `find_product(arr)` that calculates the product of all non-zero elements in a potentially nested 3D array `arr`. If the array is empty or null, the function should return 1. The function should not use library functions for multiplication and recursion.
"""

def find_product(arr):
    # Handling empty or null array
    if not arr:
        return 1

    # Handling non-zero elements
    multi = 1
    for elem in arr:
        # if the current element is a list (3D array handling)
        if isinstance(elem, list):
            multi *= find_product(elem)
        # if the current element is not zero
        elif elem != 0:
            multi *= elem
    return multi