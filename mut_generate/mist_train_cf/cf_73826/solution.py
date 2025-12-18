"""
QUESTION:
Implement a function named `fibonacci(n, memo = {})` that calculates the nth Fibonacci number efficiently using memoization. The function should handle Fibonacci numbers for large number of terms, specifically up to `n = 1000`. The function should take two parameters: `n`, the term number, and `memo`, a dictionary that stores previously computed Fibonacci numbers.
"""

def fibonacci(n, memo = {}):
    # Check if value already exists in memo
    if n in memo:
        return memo[n]
    # Base Case
    elif n <= 2:
        return 1
    # Recursive Case
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]