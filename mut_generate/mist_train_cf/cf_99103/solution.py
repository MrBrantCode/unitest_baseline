"""
QUESTION:
Write a function called `fibonacci_memoization` that calculates the nth Fibonacci number using memoization and determines the maximum value of "n" that can be passed as an argument without causing a stack overflow or memory error. The function should take an integer "n" and an optional dictionary "cache" as arguments. The function should return the nth Fibonacci number. 

The `fibonacci_memoization` function should use memoization to store the results of expensive function calls and return the cached result when the same inputs occur again. The function should also be able to handle large values of "n" without causing a stack overflow or memory error. 

Restrictions: The solution should be implemented in Python.
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