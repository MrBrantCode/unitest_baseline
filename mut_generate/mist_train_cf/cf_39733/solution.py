"""
QUESTION:
Create a Python decorator called `log_execution_time` that logs the execution time of a function and prints the result to the console. The decorator should handle functions with any number of arguments and keyword arguments, and it should also handle functions that return a value or do not return anything. The output should include the function's name and execution time, and if a value is returned, it should also include the result. If no value is returned, the output should indicate that. The execution time should be rounded to four decimal places.
"""

import time
import functools

def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = round(end_time - start_time, 4)
        if result is not None:
            print(f"{func.__name__} took {execution_time} seconds to execute and returned {result}")
        else:
            print(f"{func.__name__} took {execution_time} seconds to execute")
        return result
    return wrapper