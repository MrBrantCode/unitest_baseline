"""
QUESTION:
Write a function called `double_and_transpose` that takes a 2D array as input, doubles each item in the array, and returns a new 2D array with the doubled values in a transposed order. The function should use a nested list comprehension and return the result.
"""

def double_and_transpose(arr):
    """
    This function takes a 2D array, doubles each item, and returns a new 2D array 
    with the doubled values in a transposed order.

    Args:
        arr (list): A 2D list of integers.

    Returns:
        list: A new 2D list with the doubled values in a transposed order.
    """
    return [[2 * arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]