"""
QUESTION:
Write a function named `get_last_element` that retrieves the last element from a given deque in Python. The function should take one argument, a deque object, and return the last element. The deque may contain any type of elements and can be of any size. The function should use constant time complexity, O(1), for the retrieval operation.
"""

from collections import deque

def get_last_element(d):
    """
    Retrieves the last element from a given deque in constant time complexity, O(1).
    
    Args:
        d (deque): A deque object containing elements of any type.
    
    Returns:
        The last element in the deque.
    """
    return d[-1]