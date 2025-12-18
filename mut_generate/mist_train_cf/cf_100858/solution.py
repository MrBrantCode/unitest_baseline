"""
QUESTION:
Write a function `element_wise_multiply` that takes two input arrays of the same length and returns a new array containing the element-wise product of the input arrays, but only includes products that exceed 10.
"""

def element_wise_multiply(array1, array2):
    """
    This function performs element-wise multiplication of two input arrays and returns a new array 
    containing only the products that exceed 10.

    Args:
        array1 (list): The first input array.
        array2 (list): The second input array.

    Returns:
        list: A new array containing the element-wise products that exceed 10.
    """
    return [x * y for x, y in zip(array1, array2) if x * y > 10]