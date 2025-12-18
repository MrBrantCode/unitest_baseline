"""
QUESTION:
Write a function `fib(n)` that calculates the nth Fibonacci number for 1 ≤ n ≤ 1000 using an efficient approach to handle large inputs.
"""

def fibonacci(n, memo={0: 0, 1: 1}): 
    if n not in memo: 
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo) 
    return memo[n]