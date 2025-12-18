"""
QUESTION:
Implement a function `fibonacci(n, memo={})` that generates the nth number in the Fibonacci sequence using memoization. The function should take an integer `n` as input, use a single recursive call to compute each Fibonacci number, and optimize performance by utilizing memoization. The function should not use any built-in functions or libraries for mathematical operations.
"""

def fibonacci(n, memo={}):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]