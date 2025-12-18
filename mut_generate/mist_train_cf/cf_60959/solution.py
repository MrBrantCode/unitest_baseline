"""
QUESTION:
Implement a recursive function named `fibonacci` that generates the Fibonacci sequence up to a given number `n`. The function should handle large numbers without exceeding Python's computational limitations. Note that the function should use memoization to optimize performance.
"""

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]