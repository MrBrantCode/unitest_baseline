"""
QUESTION:
Write a function `is_power_of_two` that takes an integer `n` as input and returns `True` if `n` is a power of two, and `False` otherwise. The function should have a time complexity of O(log n) and a space complexity of O(1).
"""

def is_power_of_two(n):
    """
    Checks if a number is a power of two.
    
    Args:
        n (int): The input number to check.
    
    Returns:
        bool: True if n is a power of two, False otherwise.
    """
    if n <= 0:
        return False
    while n > 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True