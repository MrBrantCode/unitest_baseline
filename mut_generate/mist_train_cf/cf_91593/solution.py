"""
QUESTION:
Implement a function `fibonacci(n)` to calculate the nth Fibonacci number using memoization, where `n` is a non-negative integer. The function should utilize a cache to store previously computed Fibonacci numbers, reducing redundant computations. The function's time complexity should be linear, i.e., O(n).
"""

def fibonacci(n, fib_cache = {}):
    if n in fib_cache:
        return fib_cache[n]
    
    if n == 0:
        fib_cache[0] = 0
        return 0
    elif n == 1:
        fib_cache[1] = 1
        return 1
    
    fib_cache[n] = fibonacci(n-1, fib_cache) + fibonacci(n-2, fib_cache)
    
    return fib_cache[n]