"""
QUESTION:
Implement a Python decorator named `measure_execution_time` that measures the execution time of a given function and prints the elapsed time in milliseconds. The decorator should support both synchronous and asynchronous functions. For synchronous functions, use the `time` module to measure the execution time, and for asynchronous functions, use `asyncio` to measure the execution time. The decorator should work for functions with any number of positional and keyword arguments.
"""

import time
import asyncio
from functools import wraps
from typing import Callable, Any

def measure_execution_time(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time() if not asyncio.iscoroutinefunction(func) else time.monotonic()
        result = await func(*args, **kwargs)
        end_time = time.time() if not asyncio.iscoroutinefunction(func) else time.monotonic()
        elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds
        print(f"Execution time for {func.__name__}: {elapsed_time} ms")
        return result
    return wrapper