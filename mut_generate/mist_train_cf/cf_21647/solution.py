"""
QUESTION:
Write a function `get_max_value` that takes an array of integers as input and returns the maximum value considering only the first occurrence of each duplicate value. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array.
"""

def get_max_value(arr):
    """
    Returns the maximum value considering only the first occurrence of each duplicate value.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The maximum value.
    """
    if not arr:
        return None

    max_value = arr[0]
    for num in arr[1:]:
        if num > max_value:
            max_value = num
        elif num == max_value:
            continue

    return max_value