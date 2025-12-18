"""
QUESTION:
Create a decorator named `log_execution_time` that can wrap any function with any number of positional and keyword arguments, and logs the function's name, its arguments, execution time, and return value to the console, while preserving the original function's return value. The decorator should be reusable and applicable to any function without modifying its functionality.
"""

import time
from functools import wraps

def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        arg_values = ', '.join([repr(arg) for arg in args] + [f'{key}={value!r}' for key, value in kwargs.items()])
        print(f"Function '{func.__name__}' called with arguments: {arg_values}")
        print(f"Execution time: {execution_time:.6f} seconds")
        print(f"Return value: {result}")
        return result
    return wrapper