"""
QUESTION:
Implement a function named `fibonacci(n, memo={})` that calculates the nth Fibonacci number using recursion with memoization. The function should be able to handle large inputs (e.g., n = 150) efficiently by storing previously computed Fibonacci numbers in the `memo` dictionary. The base cases for the recursion are when `n` is 0 or 1.
"""

def fibonacci(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        result = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        memo[n] = result
        return result