"""
QUESTION:
Create a function called `find_min_product` that takes a list of integers as input and returns the product of the smallest non-contiguous sub-array within the list. A non-contiguous sub-array is defined as a sub-array with more than one element where the elements are not adjacent in the original list. The function should handle lists of any size, but note that the time complexity may increase exponentially with the size of the input list.
"""

from itertools import combinations 

def find_min_product(arr):
    """
    This function calculates the product of the smallest non-contiguous sub-array within the given list of integers.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    int: The product of the smallest non-contiguous sub-array.
    """
    
    min_product = float('inf')

    # Generate all possible non-contiguous sub-arrays
    sub_arrays = [list(combinations(arr,i)) for i in range(len(arr)+1)]

    # Flat the list of all sub-arrays
    sub_arrays = [item for sublist in sub_arrays for item in sublist]

    # Remove sub-arrays that contain only one element
    sub_arrays = [sub_arr for sub_arr in sub_arrays if len(sub_arr) > 1]

    # Calculate the product and find the smallest one
    for sub_arr in sub_arrays:
        product = 1
        for num in sub_arr:
            product *= num
        if product < min_product:
            min_product = product

    return min_product