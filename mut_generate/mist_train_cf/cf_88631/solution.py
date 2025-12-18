"""
QUESTION:
Create a function decorator named `logger` that logs the function name, arguments passed to the function, return value, and time taken for each function call. The decorator should calculate the time taken using only built-in Python functionalities without relying on external libraries or modules. The arguments passed should be logged in a string format, including both positional and keyword arguments, and the time taken should be logged with six decimal places.
"""

import time
from functools import wraps

def entrance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        arg_str = ', '.join([repr(arg) for arg in args] +
                           [f"{key}={repr(value)}" for key, value in kwargs.items()])
        
        print(f"Called {func.__name__}({arg_str})")
        print(f"Returned: {result}")
        print(f"Time taken: {elapsed_time:.6f} seconds\n")
        
        return result
    return wrapper