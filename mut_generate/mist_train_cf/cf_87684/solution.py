"""
QUESTION:
Implement a function `check_copy` that takes two lists `a` and `b` as input and returns `True` if they are the same object in memory and `False` otherwise. In your solution, explain the difference between shallow copy and deep copy, and provide examples to demonstrate the difference. The `check_copy` function should not modify the input lists.
"""

def check_copy(a, b):
    """
    Checks if two lists are the same object in memory.

    Args:
    a (list): The first list.
    b (list): The second list.

    Returns:
    bool: True if a and b are the same object in memory, False otherwise.
    """
    return a is b