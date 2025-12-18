"""
QUESTION:
Write a function `flatten_and_sort(arr)` that takes a two-dimensional array as input, flattens it into a one-dimensional array, removes any duplicate elements, and sorts the resulting array in ascending order.

The function should have a time complexity of O(n^2) and a space complexity of O(n), where n is the total number of elements in the input array.
"""

def flatten_and_sort(arr):
    """
    This function takes a two-dimensional array as input, 
    flattens it into a one-dimensional array, removes any duplicate elements, 
    and sorts the resulting array in ascending order.

    Args:
        arr (list): A two-dimensional array

    Returns:
        list: A sorted one-dimensional array with no duplicates
    """
    flattened = []
    for sublist in arr:
        for element in sublist:
            flattened.append(element)
    
    unique_elements = set(flattened)
    sorted_array = sorted(unique_elements)
    return sorted_array