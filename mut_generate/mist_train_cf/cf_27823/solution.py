"""
QUESTION:
Create a Python decorator named `log_execution_time` that logs the execution time of a given function. The decorator should be able to handle asynchronous functions with any number of positional and keyword arguments. The decorator should print the execution time in seconds with four decimal places, and return the result of the decorated function.
"""

import time
from functools import wraps

def log_execution_time(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper