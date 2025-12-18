"""
QUESTION:
Create a function called `fibonacci(n, memo)` that calculates and returns the nth Fibonacci number using a recursive approach with memoization. The function should take an integer `n` as input and an optional dictionary `memo` with a default value of an empty dictionary `{}`. Implement the function to optimize performance by avoiding redundant calculations.
"""

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]