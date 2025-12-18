"""
QUESTION:
Create a Python decorator `log_execution_time` that calculates the execution time of a function and prints the function name, arguments, execution time in milliseconds, and result. The decorator should be able to handle functions with any number of positional and keyword arguments. Implement another function `factorial` that calculates the factorial of a given integer `n` and apply the `log_execution_time` decorator to it. The `log_execution_time` decorator should print the function name, arguments, execution time, and result. The `factorial` function should use recursion or iteration to calculate the factorial of `n`.
"""

import time
import functools

def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time_ms = (end_time - start_time) * 1000
        print(f"Function: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        print(f"Execution time: {execution_time_ms} ms")
        print(f"Result: {result}")
        return result
    return wrapper