"""
QUESTION:
Implement a function `execution_time_decorator` that takes a function `func` as input and returns a new function. The returned function should log the execution time of `func` in milliseconds when called, with a precision of two decimal places. The execution time should be printed in the format "Function '{func_name}' took {execution_time} milliseconds to execute".
"""

import time
from functools import wraps

def execution_time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000
        print(f"Function '{func.__name__}' took {execution_time:.2f} milliseconds to execute")
        return result
    return wrapper