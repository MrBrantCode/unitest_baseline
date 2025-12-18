"""
QUESTION:
Create a Python decorator named `log_execution_time` that logs the execution time of a function. The decorator should be able to handle functions with any number of arguments and return values. It must record the start time before calling the original function, call the original function, record the end time after the function has finished executing, calculate the elapsed time, and log the elapsed time using the `logging` module with the level `INFO`.
"""

import time
import logging
from functools import wraps

# Set up the logger
LOGGER = logging.getLogger(__name__)

def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        LOGGER.info(f"Function '{func.__name__}' executed in {elapsed_time:.4f} seconds")
        return result
    return wrapper