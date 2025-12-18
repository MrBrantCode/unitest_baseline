"""
QUESTION:
Write a function `find_value` to find the value at a given index of a multidimensional unordered array. The array can have any number of dimensions, and each dimension can have any number of elements. The index can be any valid index within the array bounds. The function should work with arrays containing duplicate values.

Restriction: Analyze the time and space complexity of the function.
"""

def find_value(array, indices):
    """
    This function finds the value at a given index of a multidimensional unordered array.

    Args:
    array (list): A multidimensional array.
    indices (list): A list of indices.

    Returns:
    The value at the specified index.
    """
    value = array
    for index in indices:
        value = value[index]
    return value