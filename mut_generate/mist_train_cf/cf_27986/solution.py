"""
QUESTION:
Create a Python decorator named `measure_execution_time` that measures the execution time of a given function and prints the result in milliseconds. The decorator should be able to handle both synchronous and asynchronous functions, as well as functions with any number of positional and keyword arguments. The decorator should use the `time` module for synchronous functions and the `time` and `asyncio` modules for asynchronous functions.
"""

import time
import asyncio
from functools import wraps

def measure_execution_time(func):
    if asyncio.iscoroutinefunction(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            result = await func(*args, **kwargs)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(f"Execution time of {func.__name__}: {execution_time} ms")
            return result
    else:
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(f"Execution time of {func.__name__}: {execution_time} ms")
            return result
    return wrapper