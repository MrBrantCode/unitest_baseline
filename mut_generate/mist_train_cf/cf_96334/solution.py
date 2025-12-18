"""
QUESTION:
Implement a function `binary_search(arr, target)` that checks whether the given element `target` is present in a sorted array `arr` or not. The array is guaranteed to be sorted in ascending order and may contain duplicate elements. The time complexity of the solution should be O(log n), where n is the size of the array.
"""

def binary_search(arr, target):
    """
    Checks whether the given element `target` is present in a sorted array `arr` or not.
    
    Parameters:
    arr (list): A sorted list of elements in ascending order.
    target: The element to be searched in the array.
    
    Returns:
    bool: True if the target element is found, False otherwise.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False