"""
QUESTION:
Create a Python decorator named `log_execution_time` that logs the execution time of a function in milliseconds using the `logging` module. The decorator should work with any function, taking into account the function's arguments and return value. Use the `logging` module to log the execution time. Assume the `logging` module has already been configured to display logs.
"""

import logging
import time
from functools import wraps

LOGGER = logging.getLogger(__name__)

def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time_ms = (end_time - start_time) * 1000
        LOGGER.info(f"Function '{func.__name__}' executed in {execution_time_ms:.2f} milliseconds")
        return result
    return wrapper