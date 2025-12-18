"""
QUESTION:
Implement a function named `fibonacci` that takes an integer `n` and an optional dictionary `memo` as input, and returns the nth number in the Fibonacci sequence. The function should use memoization to optimize performance and only make recursive calls to compute each Fibonacci number. The base cases are when `n` is less than or equal to 0 (return 0) and when `n` is 1 (return 1).
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