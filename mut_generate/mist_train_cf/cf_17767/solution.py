"""
QUESTION:
Write a function `fibonacci(n, memo={})` that generates the nth Fibonacci number using memoization. The function should return the nth Fibonacci number, and it should only use a single recursive call to compute each Fibonacci number. The input `n` is an integer, and the function should use memoization to optimize performance.
"""

def fibonacci(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]