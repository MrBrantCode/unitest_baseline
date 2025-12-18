"""
QUESTION:
Implement a function `binary_search(arr, element)` that takes a sorted list `arr` and an integer `element` as input, and returns the index of `element` in `arr` if it exists, and -1 otherwise. The list `arr` is sorted in ascending order.
"""

def binary_search(arr, element):
    """
    Determine the index of an element in a given sorted array using binary search.

    Args:
        arr (list): A sorted list in ascending order.
        element (int): The target element to be searched.

    Returns:
        int: The index of the element if found, -1 otherwise.
    """
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if element < arr[mid]:
            end = mid - 1
        elif element > arr[mid]:
            start = mid + 1
        else:
            return mid
    
    return -1