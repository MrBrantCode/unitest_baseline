"""
QUESTION:
Design a decorator function named `log_decorator` that, when applied to a given function, logs the running time of the function, the number of times it was called, and any exceptions it raises while executing. The decorator should use a custom logging strategy, without relying on built-in logging or time tracking modules. The decorator should print the total call count, last execution time, and total execution time after each function call. If an exception occurs, it should print the exception message before re-raising it.
"""

import time
from functools import wraps

def log_decorator(func):
    """
    A decorator to log the running time, call count and exceptions of a function.

    Args:
        func: The function to be decorated.

    Returns:
        A wrapper function that logs the running time, call count and exceptions.
    """
    call_count = 0
    total_time = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal call_count
        nonlocal total_time
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f'Exception occurred in function {func.__name__}: {str(e)}')
            raise

        call_count += 1
        end_time = time.time()
        total_time += end_time - start_time
        print(f'Function {func.__name__} called. Total call count: {call_count}. '
              f'Last execution time: {end_time - start_time}. '
              f'Total execution time: {total_time}')
        return result

    return wrapper