"""
QUESTION:
Implement a function `recursiveSum` that calculates the sum of all integers from 0 to `n` using recursion without any loops or global variables. The function should take an integer `n` as input and return the sum of integers from 0 to `n`.
"""

def recursive_sum(n: int) -> int:
    """
    This function calculates the sum of all integers from 0 to n using recursion.

    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of integers from 0 to n.
    """
    # Base case: If n is 0, return 0
    if n == 0:
        return 0
    
    # Recursive case: Return the sum of n and recursive_sum(n-1)
    return n + recursive_sum(n-1)