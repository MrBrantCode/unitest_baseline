"""
QUESTION:
Write a function `find_value` that takes a multidimensional unordered array and an index as input, and returns the value at that index. The array can have any number of dimensions and the index should be a list or tuple of coordinates. Assume the input index is valid.
"""

def find_value(array, index):
    """
    This function takes a multidimensional unordered array and an index as input, 
    and returns the value at that index.

    Args:
        array (list): A multidimensional unordered array.
        index (list or tuple): A list or tuple of coordinates.

    Returns:
        any: The value at the given index in the array.
    """
    current = array
    for i in index:
        current = current[i]
    return current