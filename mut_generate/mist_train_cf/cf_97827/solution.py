"""
QUESTION:
Write a function named `fibonacci` that calculates the nth Fibonacci number using memoization to optimize performance. The function should store calculated Fibonacci numbers in a cache to avoid redundant calculations. The function takes an integer `n` as input and returns the nth Fibonacci number.
"""

def fibonacci(n):
    fib_cache = {0: 0, 1: 1}
    if n in fib_cache:
        return fib_cache[n]
    
    for i in range(2, n + 1):
        fib_cache[i] = fib_cache[i-1] + fib_cache[i-2]
    
    return fib_cache[n]