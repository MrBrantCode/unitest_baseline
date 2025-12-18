"""
QUESTION:
Write a Python decorator called `memoize` that caches the results of function calls. The `memoize` function should take in a function `func` as an argument, and return a new function `memoized_func` that caches the results of `func`. The cache should be implemented as a dictionary where the keys are the arguments to `func` and the values are the corresponding results. If `func` is called with arguments that are already in the cache, `memoized_func` should return the cached result instead of calling `func`.
"""

def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return memoized_func