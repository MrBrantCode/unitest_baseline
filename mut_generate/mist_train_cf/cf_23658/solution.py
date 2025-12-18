"""
QUESTION:
Write a function `two_sum_exists` that takes an array of integers `arr` and an integer `target_sum` as input. The function should return `True` if there exist at least two distinct elements in the array that add up to `target_sum`, and `False` otherwise.
"""

def two_sum_exists(arr, target_sum):
    """
    Returns True if there exist at least two distinct elements in the array that add up to target_sum, and False otherwise.

    Args:
        arr (list): A list of integers.
        target_sum (int): The target sum.

    Returns:
        bool: Whether there exist two distinct elements that add up to target_sum.
    """
    for i in range(len(arr)-1): 
        for j in range(i+1, len(arr)): 
            if arr[i] + arr[j] == target_sum: 
                return True 
    return False