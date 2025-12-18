"""
QUESTION:
Write a function `f(x)` that takes an integer `x` as input, uses a cache to store previously computed results, and returns a list containing the values of `x`, `x*2`, and `x` raised to the power of `x*2`. The function should use the cache to avoid repeated computations.
"""

def entrance(x, cache={}):
    if x not in cache:
        y = x * 2
        z = x ** y
        cache[x] = [x, y, z]
    return cache[x]