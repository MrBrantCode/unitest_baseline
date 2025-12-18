"""
QUESTION:
Write a function called `is_good_pair` that takes two integers `a` and `b` as input. The function should return `True` if the sum of `a` and `b` is even and their product is odd, and `False` otherwise.
"""

def is_good_pair(a, b):
    """
    Returns True if the sum of a and b is even and their product is odd, False otherwise.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.
    
    Returns:
        bool: Whether the pair is good or not.
    """
    return (a + b) % 2 == 0 and (a * b) % 2 != 0