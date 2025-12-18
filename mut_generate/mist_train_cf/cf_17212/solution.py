"""
QUESTION:
Find the maximum value in a multidimensional array with an arbitrary number of dimensions and sizes, and return the maximum value along with its indices. The function should only use a single loop and have a time complexity of O(N), where N is the total number of elements in the array. The function name should be `find_max_value` and it should take one argument, the multidimensional array.
"""

def find_max_value(arr):
    """
    Find the maximum value in a multidimensional array with an arbitrary number of dimensions and sizes,
    and return the maximum value along with its indices.

    Args:
    arr: A multidimensional array

    Returns:
    tuple: A tuple containing the maximum value and its indices
    """
    max_value = float('-inf')
    indices = None
    def get_indices(arr, i=0, curr=[]):
        if isinstance(arr, list):
            for idx, val in enumerate(arr):
                get_indices(val, i+1, curr + [idx])
        else:
            nonlocal max_value, indices
            if arr > max_value:
                max_value = arr
                indices = curr
    get_indices(arr)
    return max_value, indices