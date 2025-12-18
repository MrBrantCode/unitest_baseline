"""
QUESTION:
Implement the `memoize` function that takes a function `func` as input and returns a memoized version of that function. The memoized function should store the results of previous function calls in a cache (dictionary) and return the cached result if the same inputs occur again. The `memoize` function should work with functions that take any number of arguments, and the cache should be specific to each function being memoized.
"""

def memoize(func):
    cache = {}

    def memoized_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return memoized_func