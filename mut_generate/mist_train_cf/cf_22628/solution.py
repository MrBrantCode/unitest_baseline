"""
QUESTION:
Write a function `max_abs` that takes a list of integers as input and returns the maximum absolute value, excluding zero. If the list is empty or contains only zeros, the function should return None or a default value indicating no valid maximum absolute value.
"""

def max_abs(lst):
    """
    Returns the maximum absolute value in a list of integers, excluding zero.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        int or None: The maximum absolute value, or None if the list is empty or contains only zeros.
    """
    return max((abs(num) for num in lst if num != 0), default=None)