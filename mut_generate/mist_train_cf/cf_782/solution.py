"""
QUESTION:
Write a function `check_sorted` that takes a sorted array of integers in non-decreasing order and returns "pass" if the array is sorted, otherwise return the array as is. The function should have a time complexity of O(n^2).
"""

def check_sorted(arr):
    """
    This function checks if the input array is sorted in non-decreasing order.
    
    Args:
        arr (list): A list of integers.
    
    Returns:
        str or list: 'pass' if the array is sorted, otherwise the array as is.
    """
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                return arr
    return "pass"