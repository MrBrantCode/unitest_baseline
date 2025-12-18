"""
QUESTION:
Implement a function `binary_search` that takes a sorted list of integers and a target integer, and returns the index of the target integer if it exists in the list, or -1 otherwise. The function must have a time complexity of O(log n), where n is the length of the list, and it must be implemented using a recursive approach without using any built-in sorting or searching functions.
"""

def binary_search(arr, target):
    """
    Searches for the target integer in a sorted list of integers using a recursive binary search approach.

    Args:
        arr (list): A sorted list of integers.
        target (int): The target integer to search for.

    Returns:
        int: The index of the target integer if it exists in the list, or -1 otherwise.
    """
    def binary_search_helper(arr, target, low, high):
        if low > high:
            return -1
        
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_helper(arr, target, mid + 1, high)
        else:
            return binary_search_helper(arr, target, low, mid - 1)

    return binary_search_helper(arr, target, 0, len(arr) - 1)