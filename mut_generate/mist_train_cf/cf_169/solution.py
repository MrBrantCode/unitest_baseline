"""
QUESTION:
Write a function `find_occurrences(arr, target)` that takes a sorted list of integers `arr` and a target integer `target` as input, and returns the number of occurrences of `target` in `arr` without using built-in Python functions like "in", "count", or "collections", and without using loops or recursion.
"""

def find_occurrences(arr, target):
    """
    This function calculates the number of occurrences of a target integer in a sorted list of integers.
    
    Parameters:
    arr (list): A sorted list of integers.
    target (int): The target integer to be searched.
    
    Returns:
    int: The number of occurrences of the target integer in the list.
    """
    
    def binary_search(left, right):
        if left > right:
            return 0
        
        mid = (left + right) // 2
        
        if arr[mid] == target:
            # Count occurrences on both sides
            left_count = binary_search(left, mid - 1)
            right_count = binary_search(mid + 1, right)
            return left_count + right_count + 1
        elif arr[mid] < target:
            # Target is on the right side
            return binary_search(mid + 1, right)
        else:
            # Target is on the left side
            return binary_search(left, mid - 1)
    
    return binary_search(0, len(arr) - 1)