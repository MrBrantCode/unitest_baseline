"""
QUESTION:
Determine the time complexity of selection sort, bubble sort, and insertion sort when the input array is in reverse order and has duplicate elements, with each element needing to be shifted to its correct position. Implement a function `sorting_complexity` that returns the time complexity of these algorithms under these conditions.
"""

def sorting_complexity(n):
    """
    Returns the time complexity of selection sort, bubble sort, and insertion sort 
    when the input array is in reverse order and has duplicate elements.

    Args:
        n (int): The number of elements in the input array.

    Returns:
        str: The time complexity of the sorting algorithms.
    """
    return f"O({n}^2)"