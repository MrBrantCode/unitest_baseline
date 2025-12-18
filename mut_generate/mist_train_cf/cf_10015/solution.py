"""
QUESTION:
Create a function named `create_array` that generates an array of integers from 0 to n-1, where n is a positive integer and can be as large as 10^6.
"""

def create_array(n):
    """
    Generate an array of integers from 0 to n-1.

    Args:
        n (int): A positive integer.

    Returns:
        list: An array of integers from 0 to n-1.
    """
    return list(range(n))