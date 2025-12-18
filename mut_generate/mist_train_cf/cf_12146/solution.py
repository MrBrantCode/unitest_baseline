"""
QUESTION:
Write a function called `swap_numbers` that takes two integers `a` and `b` as input and returns the swapped values of `a` and `b` without using a temporary variable. The function should have a time complexity of O(1).
"""

def swap_numbers(a, b):
    """
    This function swaps the values of two integers without using a temporary variable.
    
    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    
    Returns:
    tuple: A tuple containing the swapped values of a and b.
    """
    a = a + b
    b = a - b
    a = a - b
    return a, b