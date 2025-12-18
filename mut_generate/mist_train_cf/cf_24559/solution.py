"""
QUESTION:
Write a function `reverseStack` that takes a stack of integers as input and returns a new stack with the elements in reverse order. The original stack should be empty after the operation. Implement this function without using any external libraries other than the standard stack library.
"""

def reverse_stack(s):
    """
    Reverses the elements of a given stack.

    Args:
    s (list): The input stack.

    Returns:
    list: A new stack with elements in reverse order.
    """
    temp_stack = []
    while s:
        temp_stack.append(s.pop())
    return temp_stack