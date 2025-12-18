"""
QUESTION:
Create a Python decorator function named `timed_execution` that takes a log level as an argument. The decorator should log the start and end time of a function's execution, as well as any exceptions that occur, using the provided log level. The log messages should include the function name, execution time, and any exception information. The decorator should use the `logging` module and allow the user to specify the log level for the messages.
"""

import logging
import time
from functools import wraps

def timed_execution(log_level=logging.INFO):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(func.__name__)
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                end_time = time.time()
                logger.log(log_level, f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
                return result
            except Exception as e:
                end_time = time.time()
                logger.log(log_level, f"{func.__name__} execution failed: {e}, executed in {end_time - start_time:.4f} seconds")
                raise
        return wrapper
    return decorator