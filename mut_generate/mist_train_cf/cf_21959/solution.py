"""
QUESTION:
Write a function named `sum_even` that calculates the sum of all even integers from 1 to a given number `n` with a time complexity of O(1).
"""

def sum_even(n):
    """
    Calculate the sum of all even integers from 1 to a given number n with a time complexity of O(1).
    
    Args:
    n (int): The upper limit.

    Returns:
    int: The sum of all even integers from 1 to n.
    """
    last_term = n if n % 2 == 0 else n - 1  # The last even term
    count = last_term // 2  # The count of even terms
    return count * (2 + last_term)  # Sum of even terms using the formula