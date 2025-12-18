"""
QUESTION:
Create a function `fibonacci` that calculates the nth Fibonacci number using recursion and memoization. The function should take an integer `n` as input and return the corresponding Fibonacci number. It should use a dictionary to store previously computed results to improve performance.
"""

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]