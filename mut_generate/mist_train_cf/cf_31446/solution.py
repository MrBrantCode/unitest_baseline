"""
QUESTION:
Create a Python decorator named `timer` that takes a function as an argument and returns a wrapper function. The wrapper function should measure the time taken to execute the input function and print the total time in seconds. The `timer` decorator should be able to handle functions with any number of positional and keyword arguments. Use the `time` module for time measurement.
"""

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        total = time.time() - start
        print("Time:", total)
        return rv
    return wrapper