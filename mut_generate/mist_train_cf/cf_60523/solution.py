"""
QUESTION:
Write a Python function `memoize` that takes a function `f` as input and returns a memoized version of `f`. The memoized version should store the results of previous function calls and reuse them when the same inputs occur again to improve the efficiency of recursive algorithms.
"""

def memoize(f):
    """
    A function that returns a memoized version of the input function f.
    
    Args:
    f (function): The function to be memoized.
    
    Returns:
    function: A memoized version of f.
    """
    cache = dict()
    
    def memoized_func(*args):
        if args in cache:
            return cache[args]
        else:
            result = f(*args)
            cache[args] = result
            return result
    
    return memoized_func