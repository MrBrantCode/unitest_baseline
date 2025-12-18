"""
QUESTION:
Create a Python decorator named `rate_limit` that limits the rate at which a function can be called. The decorator should take two arguments: `max_calls` (the maximum number of calls allowed) and `period` (the time period in seconds). The decorator should enforce the rate limit using asyncio's `sleep` function.
"""

import asyncio
import time
from functools import wraps

def rate_limit(max_calls: int, period: int):
    """
    A decorator that limits the rate at which a function can be called.
    """
    def decorator(func):
        call_times = []
        @wraps(func)
        async def wrapper(*args, **kwargs):
            now = time.monotonic()
            # Remove old call times from the list
            while call_times and call_times[0] < now - period:
                call_times.pop(0)
            # Check if the maximum number of calls has been reached
            if len(call_times) >= max_calls:
                sleep_time = period - (now - call_times[0])
                await asyncio.sleep(sleep_time)
            call_times.append(now)
            return await func(*args, **kwargs)
        return wrapper
    return decorator