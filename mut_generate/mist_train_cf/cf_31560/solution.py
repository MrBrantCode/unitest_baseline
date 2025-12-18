"""
QUESTION:
Implement a decorator `cache_result` that caches the result of a function and returns the cached result if the function is called with the same arguments. The decorator should work for functions with any number of arguments and keyword arguments, support caching multiple function calls with different arguments, handle mutable arguments and keyword arguments correctly, and not cache the result if the function raises an exception.
"""

import functools

def cache_result(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        try:
            result = func(*args, **kwargs)
            cache[key] = result
            return result
        except Exception as e:
            if key in cache:
                del cache[key]
            raise e

    return wrapper