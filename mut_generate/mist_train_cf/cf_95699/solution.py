"""
QUESTION:
Create a function named `logger` that takes another function `func` as its argument and returns a wrapper function. The `logger` function should log the following information for each call to `func`: the name of the function being called, the arguments passed to the function (including both positional and keyword arguments), the return value of the function, and the time taken for the function call. The wrapper function should also preserve the original function's metadata and return its result.
"""

import functools
import time
from logging import getLogger

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        arguments = [repr(arg) for arg in args]
        arguments.extend(f"{key}={repr(value)}" for key, value in kwargs.items())
        arguments = ", ".join(arguments)

        getLogger().info(f"Calling {func.__name__}({arguments})")
        getLogger().info(f"Return value: {result}")
        getLogger().info(f"Time taken: {execution_time} seconds")
        return result

    return wrapper