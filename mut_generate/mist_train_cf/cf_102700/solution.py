"""
QUESTION:
Write a function `hasDuplicates` that takes an array of integers as input and returns `True` if there are any duplicate elements in the array, and `False` otherwise. The function should have a time complexity of O(n), where n is the number of elements in the input array.
"""

def has_duplicates(arr):
    """
    Checks if there are any duplicate elements in the input array.
    
    Args:
    arr (list): A list of integers.
    
    Returns:
    bool: True if there are any duplicate elements, False otherwise.
    """
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False