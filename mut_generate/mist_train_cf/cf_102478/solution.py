"""
QUESTION:
Write a function `sum_even_integers(n)` that calculates the sum of all even integers from 1 to `n`. The function must have a time complexity of O(1) and a space complexity of O(1).
"""

def sum_even_integers(n):
    """
    Calculate the sum of all even integers from 1 to n.

    Args:
    n (int): The upper limit of the range of even integers.

    Returns:
    int: The sum of all even integers from 1 to n.

    """
    return n * (n + 2) // 4 if n % 2 == 0 else (n - 1) * (n + 1) // 4