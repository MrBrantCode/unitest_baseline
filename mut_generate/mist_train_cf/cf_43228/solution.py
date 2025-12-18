"""
QUESTION:
Create a Python decorator named `log_execution` that logs the execution time, arguments, and return value of a function. The decorator should be able to handle both synchronous and asynchronous functions. The decorator should be reusable for any function with any number of arguments.
"""

import time
import asyncio
import functools

def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        print(f"Function '{func.__name__}' executed in {execution_time} seconds")
        print(f"Arguments: {args}, {kwargs}")
        print(f"Return value: {result}")
        return result

    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        execution_time = time.time() - start_time
        print(f"Function '{func.__name__}' executed in {execution_time} seconds")
        print(f"Arguments: {args}, {kwargs}")
        print(f"Return value: {result}")
        return result

    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    else:
        return wrapper