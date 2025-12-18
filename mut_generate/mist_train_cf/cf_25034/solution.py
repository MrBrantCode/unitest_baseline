"""
QUESTION:
Create a function `generate_requests` that generates a list of integers from 0 to n (exclusive). The function should take an integer `n` as input and return a list of integers. Optimize the function for performance when n is large.
"""

def generate_requests(n):
    """
    Generates a list of integers from 0 to n (exclusive).

    Args:
    n (int): The upper limit of the range of integers.

    Returns:
    list: A list of integers from 0 to n (exclusive).
    """
    return [i for i in range(n)]