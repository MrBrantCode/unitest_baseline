"""
QUESTION:
Create a decorator function called `log_execution_time` that takes a function `func` as its argument. The decorator should measure the execution time of the function `func` and print the function name, execution time, and the arguments passed to the function. The decorator should work for functions with both positional and keyword arguments, handling any number of arguments and keyword arguments. Use the `time` module for time measurement. The output should be in the format "Function '{func_name}' executed in {execution_time:.4f} seconds with arguments ({arguments})".
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
        args_str = ', '.join(map(repr, args))
        kwargs_str = ', '.join(f"{k}={v!r}" for k, v in kwargs.items())
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds with arguments ({all_args})")
        return result
    return wrapper