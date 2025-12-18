"""
QUESTION:
Write a function `reverse_clone_array` that takes an array as input, clones it, and returns the cloned array with its elements in reverse order. The function should not modify the original array.
"""

def reverse_clone_array(arr):
    """
    Clone the input array and return the cloned array with its elements in reverse order.

    Args:
        arr (list): The input array.

    Returns:
        list: A cloned array with elements in reverse order.
    """
    return arr[::-1]