"""
QUESTION:
Implement a recursive function `factorial(n)` in Python to calculate the factorial of a given number `n`. The function should be able to handle large numbers efficiently without using excessive memory.
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