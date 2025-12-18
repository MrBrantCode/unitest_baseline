"""
QUESTION:
Create a Python decorator named `log_execution_time` that can be applied to any function with any number of arguments and keyword arguments. The decorator should calculate the execution time of the decorated function and print it to the console. The execution time should be printed in seconds with six decimal places, and the function name should be included in the print statement. The decorator should return the result of the decorated function.
"""

import time

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds")
        return result
    return wrapper