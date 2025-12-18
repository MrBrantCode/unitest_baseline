"""
QUESTION:
Write a function named `fibonacci` that calculates the nth Fibonacci number using recursion with a time complexity of O(n), where n is the input number. The function should use memoization to optimize performance.
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