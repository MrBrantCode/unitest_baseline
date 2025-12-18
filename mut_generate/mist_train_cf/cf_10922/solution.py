"""
QUESTION:
Write a function named `fibonacci` that calculates the nth Fibonacci number using memoization. The function should take an integer `n` as input and return the corresponding Fibonacci number. The function should use a memoization technique to store previously computed Fibonacci numbers and reuse them to avoid redundant computations. The function should have a time complexity of O(n).
"""

def fibonacci(n, fib_cache = {}):
    # If the Fibonacci number is already computed, return it from the cache
    if n in fib_cache:
        return fib_cache[n]
    
    # Base cases
    if n == 0:
        fib_cache[0] = 0
        return 0
    elif n == 1:
        fib_cache[1] = 1
        return 1
    
    # Compute the Fibonacci number using memoization
    fib_cache[n] = fibonacci(n-1, fib_cache) + fibonacci(n-2, fib_cache)
    
    return fib_cache[n]