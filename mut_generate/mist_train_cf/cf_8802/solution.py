"""
QUESTION:
Implement a memoized version of the Fibonacci sequence function, which calculates the nth Fibonacci number using memoization to optimize performance by avoiding redundant computations. The function should take an integer `n` as input and return the corresponding Fibonacci number. Implement the function with a cache to store previously computed results.
"""

def fibonacci(n, memo={}):
    """
    This function calculates the nth Fibonacci number using memoization.
    
    Args:
    n (int): The position of the Fibonacci number to be calculated.
    memo (dict): A dictionary to store previously computed Fibonacci numbers. Defaults to {}.
    
    Returns:
    int: The nth Fibonacci number.
    """
    if n in memo:
        # If the Fibonacci number is already in the cache, return it directly
        return memo[n]
    if n <= 2:
        # Base case: The first two Fibonacci numbers are 1
        return 1
    # If the Fibonacci number is not in the cache, calculate it recursively
    # and store the result in the cache
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]