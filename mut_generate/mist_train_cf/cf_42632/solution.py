"""
QUESTION:
Create a Python decorator named `measure_execution_time` that can be used to measure the execution time of both synchronous and asynchronous functions. The decorator should print the execution time in milliseconds. If the function returns a value, the decorator should also print the returned value. If the function raises an exception, the decorator should catch the exception, print an error message, and re-raise the exception. The decorator should handle both synchronous and asynchronous functions, and should not modify the original function's behavior or return value.
"""

import time
import asyncio
from functools import wraps

def measure_execution_time(func):
    @wraps(func)
    async def async_wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = await func(*args, **kwargs)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(f"Execution time: {execution_time:.2f} ms")
            if result is not None:
                print(f"Returned value: {result}")
            return result
        except Exception as e:
            print(f"Error: {e}")
            raise

    def sync_wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            print(f"Execution time: {execution_time:.2f} ms")
            if result is not None:
                print(f"Returned value: {result}")
            return result
        except Exception as e:
            print(f"Error: {e}")
            raise

    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    else:
        return sync_wrapper