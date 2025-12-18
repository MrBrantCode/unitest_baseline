"""
QUESTION:
Implement a function called "first_duplicate" that takes an array of integers as input and returns the first duplicate element found in the array. If no duplicate is found, the function should return -1. The function should have a time complexity of O(n), where n is the length of the array.
"""

def first_duplicate(arr):
    """
    This function finds the first duplicate element in an array of integers.
    
    Args:
    arr (list): A list of integers.
    
    Returns:
    int: The first duplicate element found in the array. If no duplicate is found, returns -1.
    """
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return -1