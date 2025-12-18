"""
QUESTION:
Implement a function named `factorial` that calculates the factorial of a given number `n`. The function should be recursive, handle large numbers efficiently, and use minimal memory.
"""

def factorial(n, cache={}):
    if n in cache:
        return cache[n]
    elif n == 0:
        return 1
    else:
        result = n * factorial(n-1, cache)
        cache[n] = result
        return result