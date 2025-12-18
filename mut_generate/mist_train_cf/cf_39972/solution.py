"""
QUESTION:
Implement a Python decorator named `cache` that caches the result of a function call to improve performance. The decorator should be able to handle functions with any number of positional and keyword arguments. The cached results should be stored in a dictionary where the key is a tuple containing the function's arguments and the value is the result of the function call. If the function is called with the same set of arguments as a previous call, the cached result should be returned instead of re-evaluating the function. The decorator should work for both pure and impure functions (functions with side effects).
"""

def cache(func):
    cached_results = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cached_results:
            cached_results[key] = func(*args, **kwargs)
        return cached_results[key]

    return wrapper