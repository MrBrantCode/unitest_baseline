"""
QUESTION:
Create a Python decorator function called `log_decorator` that records the runtime of a function, its input parameters, and its output. The decorator should not modify the original function's name and docstring, and it should be able to handle any number of positional and keyword arguments. The recorded runtime, input parameters, and output should be printed to the console.
"""

import time
from functools import wraps

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"Function {func.__name__} ran in: {elapsed_time} seconds")
        print(f"Input parameters were: {args}, {kwargs}")
        print(f'Result was: {result}')
        return result
    return wrapper