"""
QUESTION:
Create a function `calculate` that uses recursion and memoization to calculate the factorial of a given non-negative integer `n`. The function should cache previously computed factorials to improve computational efficiency. The function should return the factorial of `n`.
"""

def calculate(n, memo={}):
    """
    Calculate the factorial of a given non-negative integer n using recursion and memoization.
    
    Args:
    n (int): A non-negative integer.
    memo (dict, optional): A dictionary to store previously computed factorials. Defaults to {}.
    
    Returns:
    int: The factorial of n.
    """
    
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    memo[n] = n * calculate(n-1, memo)
    return memo[n]