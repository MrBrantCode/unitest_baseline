"""
QUESTION:
Create a function named `create_zeros_array` that takes an existing array as input and returns a new array of the same size with all elements initialized to 0.
"""

def create_zeros_array(oldArray):
    """
    Creates a new array of the same size as the input array, with all elements initialized to 0.

    Args:
        oldArray (list): The input array.

    Returns:
        list: A new array with all elements initialized to 0.
    """
    return [0] * len(oldArray)