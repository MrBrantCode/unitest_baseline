"""
QUESTION:
Create a function named `logger` that takes in another function `func` and returns a wrapper function. The `logger` function should log the name of `func`, the arguments passed to `func`, and the return value of `func`. The `logger` function should also return the return value of `func`. Use the `functools.wraps` decorator to preserve the metadata of the original function.
"""

import functools
import logging

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function: {func.__name__}")
        logging.info(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Return value: {result}")
        return result
    return wrapper