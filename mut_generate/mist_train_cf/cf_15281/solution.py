"""
QUESTION:
Write a function `fibonacci(n, memo={})` that calculates the Fibonacci sequence up to the nth term using memoization. The function should be able to handle large numbers efficiently and should return the nth Fibonacci number.
"""

def fibonacci(n, memo={}):
    if n <= 1:
        return n
    elif n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]