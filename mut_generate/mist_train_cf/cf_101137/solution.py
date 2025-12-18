"""
QUESTION:
Implement a function named `fibonacci(n, cache={})` that takes an integer `n` and an optional dictionary `cache` as parameters, and returns the `n`th number in the Fibonacci sequence. The function should handle both positive and negative integers, and optimize its time complexity using memoization.
"""

def fibonacci(n, cache={}):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in cache:
        return cache[n]
    elif n > 1:
        result = fibonacci(n-1, cache) + fibonacci(n-2, cache)
        cache[n] = result
        return result
    else:  # n < 0
        result = fibonacci(n+2, cache) - fibonacci(n+1, cache)
        cache[n] = result
        return result