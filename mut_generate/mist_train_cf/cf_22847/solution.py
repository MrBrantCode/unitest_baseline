"""
QUESTION:
Implement a function `calculate_sum(n)` that calculates the sum of positive integers from 1 to `n` using recursion and memoization. The function should return the sum for a given positive integer `n`. Ensure the function handles recursive calls efficiently by utilizing memoization to store previously computed results.
"""

# Memoization cache
memo = {0: 0}

def calculate_sum(n):
    """
    Calculate the sum of positive integers from 1 to n using recursion and memoization.
    
    Args:
    n (int): A positive integer.
    
    Returns:
    int: The sum of positive integers from 1 to n.
    """
    if n in memo:
        return memo[n]
    else:
        memo[n] = n + calculate_sum(n - 1)
        return memo[n]