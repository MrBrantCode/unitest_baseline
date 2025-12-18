"""
QUESTION:
Create a memoization decorator named `memoized` that caches the results of a function and returns the cached result when the same inputs occur again. The decorator should work for functions with any number of arguments and handle both positional and keyword arguments. The function should return the cached result instead of recalculating it when the same inputs are provided again.
"""

import functools

def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper