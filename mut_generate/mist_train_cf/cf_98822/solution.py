"""
QUESTION:
Write a function `fibonacci(n)` that calculates the nth number of the Fibonacci sequence, where `n` can be a negative integer. The function should have a time complexity of O(n) using dynamic programming principles such as memoization. The function should handle negative integers based on the formula `F(n) = F(n+2) - F(n+1)`.
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