"""
QUESTION:
Implement a function `sqlalchemy_cache` that takes an integer `max_size` as input and returns a decorator. The returned decorator should cache the results of the decorated function in a dictionary, using the function name and arguments as the key. The cache should have a maximum size, and if it exceeds this size, the least recently used item should be removed to make space for new entries. If the same function is called with the same arguments, the decorator should return the cached result instead of executing the function again. The cache should preserve the order in which keys were last accessed.
"""

from collections import OrderedDict

def sqlalchemy_cache(max_size):
    cache = OrderedDict()

    def decorator(func):
        def wrapper(*args, **kwargs):
            key = (func.__name__, args, frozenset(kwargs.items()))
            if key in cache:
                cache.move_to_end(key)
                return cache[key]
            else:
                result = func(*args, **kwargs)
                if len(cache) >= max_size:
                    cache.popitem(last=False)  
                cache[key] = result
                return result
        return wrapper
    return decorator