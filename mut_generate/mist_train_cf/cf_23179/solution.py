"""
QUESTION:
Write a recursive function `fib` that calculates the nth Fibonacci number, and use memoization to optimize its performance. The function should take an integer `n` as input and return the corresponding Fibonacci number. Implement memoization using a cache, and ensure the function avoids redundant computations by checking the cache before making recursive calls. Assume that the input `n` is a non-negative integer.
"""

cache = {}

def fib(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    result = fib(n-1) + fib(n-2)
    cache[n] = result
    return result