"""
QUESTION:
Implement a decorator function named `execution_time_logger` that logs the execution time of a given function. The decorator should be able to handle functions with any number of arguments and keyword arguments, as well as functions that return values of any type. The decorator should print the name of the function being called and the time taken for execution in milliseconds, while preserving the original function's docstring and any additional attributes.
"""

import time
import functools

def execution_time_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # in milliseconds
        print(f"Function '{func.__name__}' executed in {execution_time:.2f} ms")
        return result
    return wrapper