"""
QUESTION:
Create a Python function `factorial` to calculate the factorial of a given positive integer `n`. The function should handle large input values without consuming too much memory.
"""

cache = {}

def factorial(n):
    if n in cache:
        return cache[n]
    if n == 0:
        return 1
    else:
        result = n * factorial(n-1)
        cache[n] = result
        return result