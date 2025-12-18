"""
QUESTION:
Write a memoized recursive function `fib(n)` to calculate the nth Fibonacci number. The function should store the results of each function call in a cache to avoid redundant computations. The cache should be implemented as a dictionary where the keys are the input values and the values are the corresponding Fibonacci numbers. 

The function should return the nth Fibonacci number and have a time complexity of O(n) instead of O(2^n).
"""

def fibonacci(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    result = fibonacci(n-1, cache) + fibonacci(n-2, cache)
    cache[n] = result
    return result