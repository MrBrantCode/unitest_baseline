"""
QUESTION:
Implement a Python decorator `timer` that measures the execution time of a given function and prints the result. The decorator should be able to handle functions with any number of positional and keyword arguments. Also, create a class `Timer` to measure the execution time of a given function. The `Timer` class should provide a context manager for measuring execution time.
"""

import time
from functools import wraps

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.execution_time = self.end_time - self.start_time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with Timer() as t:
            result = func(*args, **kwargs)
        print(f"Execution time of {func.__name__}: {t.execution_time} seconds")
        return result
    return wrapper