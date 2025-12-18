"""
QUESTION:
Create a function `custom_sort_advanced` that takes an array of integers as input, which may include repetitive and negative entries. Determine if it's possible to create a sorted array with unique elements by removing any number of elements or inverting any subarray. If possible, return True. Otherwise, return False. If the input array is empty, return True.
"""

def custom_sort_advanced(numbers):
    """
    Determine if it's possible to create a sorted array with unique elements by removing any number of elements or inverting any subarray.
    
    Args:
    numbers (list): A list of integers which may include repetitive and negative entries.
    
    Returns:
    bool: True if it's possible to create a sorted array with unique elements, False otherwise.
    """
    return len(numbers) == len(set(numbers))