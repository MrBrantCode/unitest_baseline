"""
QUESTION:
Write a function called `find_min` that takes a nested array of non-negative integers as input and returns the minimum element. The function should handle arrays with arbitrary levels and lengths, and have a time complexity of O(n), where n is the total number of elements in the array.
"""

def find_min(nested_array):
    """
    This function finds the minimum element in a nested array of non-negative integers.

    Args:
    nested_array (list): A nested array of non-negative integers.

    Returns:
    int: The minimum element in the nested array.
    """
    min_value = float('inf')

    def recursive_min(array):
        nonlocal min_value
        for element in array:
            if isinstance(element, int):
                min_value = min(min_value, element)
            elif isinstance(element, list):
                recursive_min(element)

    recursive_min(nested_array)
    return min_value