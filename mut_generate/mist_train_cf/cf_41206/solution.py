"""
QUESTION:
Create a Python decorator named `measure_execution_time` that measures the execution time of a function, handles both synchronous and asynchronous functions, and logs the result. The decorator should be able to handle functions with any number of positional and keyword arguments. If the decorated function returns a value, the decorator should print the returned value; otherwise, it should print "Function executed successfully". The execution time should be printed in milliseconds.
"""

import time
import asyncio
from functools import wraps

def measure_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        if asyncio.iscoroutinefunction(func):
            result = asyncio.run(func(*args, **kwargs))
        else:
            result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # in milliseconds
        if result is not None:
            print(f"Execution time: {execution_time} ms")
            print(f"Returned value: {result}")
        else:
            print(f"Execution time: {execution_time} ms")
            print("Function executed successfully")
    return wrapper