"""
QUESTION:
Write a function `fibonacci_memoization` that uses memoization to calculate the nth Fibonacci number without causing a stack overflow or memory error. The function should take an integer `n` as input and return the nth Fibonacci number. The function should also be able to handle large values of `n` without causing a stack overflow or memory error. 

Note: The recursion limit should be set to a large value to accommodate large values of `n`.
"""

def fibonacci_memoization(n, cache={}):
    if n in cache:
        return cache[n]
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci_memoization(n-1, cache) + fibonacci_memoization(n-2, cache)
        cache[n] = result
        return result