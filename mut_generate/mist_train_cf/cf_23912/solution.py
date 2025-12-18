"""
QUESTION:
Write a function that generates a list of numbers from 1 to n in reverse order. The function should take an integer n as input and return the list.
"""

def reverse_list(n):
    """
    Generates a list of numbers from 1 to n in reverse order.

    Args:
        n (int): The upper limit of the list.

    Returns:
        list: A list of numbers from 1 to n in reverse order.
    """
    return list(range(n, 0, -1))