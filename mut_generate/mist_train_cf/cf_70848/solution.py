"""
QUESTION:
Write a function `sort_subarrays` that takes a 2D array of numerical elements as input, sorts the elements within each sub-array in descending order, and sorts the sub-arrays themselves in descending order based on the first element of each sub-array.
"""

def sort_subarrays(arr):
    """
    Sorts the elements within each sub-array in descending order and 
    sorts the sub-arrays themselves in descending order based on the first element of each sub-array.

    Args:
        arr (list): A 2D array of numerical elements.

    Returns:
        list: The sorted 2D array.
    """

    # Sort elements within each sub-array in descending order
    arr = [sorted(sublist, reverse=True) for sublist in arr]
    
    # Sort sub-arrays based on the first element of each sub-array in descending order
    arr = sorted(arr, key=lambda x: x[0], reverse=True)

    return arr