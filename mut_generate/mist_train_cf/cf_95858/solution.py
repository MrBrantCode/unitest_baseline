"""
QUESTION:
Implement a recursive function `fibonacci(n, cache={})` to calculate the nth Fibonacci number using memoization, where `n` is a non-negative integer and `cache` is a dictionary that stores the previously calculated Fibonacci numbers. Ensure the function has a time complexity of O(n) and optimizes the code for better performance.
"""

def fibonacci(n, cache={}):
    if n in cache:
        return cache[n]
    elif n <= 1:
        return n
    else:
        result = fibonacci(n-1, cache) + fibonacci(n-2, cache)
        cache[n] = result
        return result