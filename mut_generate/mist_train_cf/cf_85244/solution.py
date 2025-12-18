"""
QUESTION:
Write a function `product_of_elements` that takes a 2D array as input and returns the product of all non-zero elements. The function should handle nested sub-arrays and ignore any zero elements. The input array can be any size and contain any number of sub-arrays.
"""

def product_of_elements(input_array):
    """
    This function calculates the product of all non-zero elements in a 2D array.

    Args:
    input_array (list): A 2D array containing integers.

    Returns:
    int: The product of all non-zero elements in the array.
    """
    prod = 1
    for i in input_array:
        for j in i:
            if j != 0:
                prod *= j
    return prod