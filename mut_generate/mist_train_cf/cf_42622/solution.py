"""
QUESTION:
Create a decorator named `decorator_pause` that takes a threshold time in seconds as an argument. This decorator should be able to handle both regular and asynchronous functions, measure their execution time, and pause the execution if it exceeds the given threshold.
"""

import asyncio
import time
from functools import wraps

def decorator_pause(threshold):
    def decorator(func):
        @wraps(func)
        async def wrapper_pause(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            if asyncio.iscoroutine(result):
                result = await result
            execution_time = time.time() - start_time
            if execution_time > threshold:
                await asyncio.sleep(execution_time - threshold)
            return result
        return wrapper_pause

    return decorator