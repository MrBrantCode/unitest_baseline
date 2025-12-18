"""
QUESTION:
Implement an efficient decorator in Python, named `my_decorator`, that optimizes memory management and runtime by avoiding unnecessary copies of decorated functions. Use `functools.wraps` to preserve the original function name and signature. The decorator should take a function as input and return a wrapped function that adds a simple logging feature, printing a message before and after the function call. The decorator should handle potential errors that may arise during function execution and log the error message with the function name.
"""

import functools
import logging

logging.basicConfig(level=logging.DEBUG)

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            print("Before function call")
            result = func(*args, **kwargs)
            print("After function call")
            return result
        except Exception as e:
            logging.exception("Error in function %s: %s", func.__name__, str(e))
    return wrapper