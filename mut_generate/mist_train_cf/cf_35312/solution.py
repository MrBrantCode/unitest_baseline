"""
QUESTION:
Write a Python decorator function named `execution_time_logger` that can handle both synchronous and asynchronous functions. The decorator should calculate the execution time of the function in milliseconds, print it to the console, and return the result of the function. The execution time should be logged with a message in the format "Execution time for {function_name}: {execution_time} ms". 

The function should work correctly for functions with any number of arguments.
"""

import time
import asyncio

def execution_time_logger(func):
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs) if asyncio.iscoroutinefunction(func) else func(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000
        print(f"Execution time for {func.__name__}: {execution_time} ms")
        return result
    return wrapper