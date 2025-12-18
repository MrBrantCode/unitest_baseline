"""
QUESTION:
Implement a custom decorator named `timer` that calculates the execution time of a function in milliseconds and prints the result, while preserving the original function's return value and metadata. The decorator should be able to handle functions with any number of arguments and keyword arguments.
"""

from time import time
from contextlib import contextmanager
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Execution time: {(end_time - start_time) * 1000} ms")
        return result
    return wrapper