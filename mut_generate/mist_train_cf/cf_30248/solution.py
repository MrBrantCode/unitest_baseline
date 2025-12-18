"""
QUESTION:
Create a Python decorator named `log_execution_time` that logs the execution time of a function. The decorator should measure the execution time, print the function name, execution time in seconds with 6 decimal places, and the arguments passed to the function. The original function's docstring and other metadata should be preserved.
"""

import time
import functools

def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds with arguments: {args}, {kwargs}")
        return result
    return wrapper