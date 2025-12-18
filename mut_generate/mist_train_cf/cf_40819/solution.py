"""
QUESTION:
Create a Python decorator function `clacks` that takes an optional argument `names`, a list of names to be included in the printed message. The decorator should measure the execution time of a given function and print the result in the specified format. If `names` is provided, the printed message should include the names; otherwise, it should include 'all_names'. The decorator should use the `time` module for measuring the execution time and the `functools.wraps` decorator to preserve the original function's metadata.
"""

import time
from functools import wraps

def entrance(names=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = f(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time

            if names:
                names_str = ', '.join(names)
            else:
                names_str = 'all_names'

            print(f"Function {f.__name__} executed in {execution_time:.6f} seconds by {names_str}")
            return result

        return wrapper

    return decorator