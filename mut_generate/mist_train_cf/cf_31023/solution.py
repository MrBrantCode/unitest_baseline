"""
QUESTION:
Implement a decorator function `timer_memory` that takes a function name as an argument and measures the execution time and memory usage of the decorated function. The function should print the time taken for execution in seconds and the memory used by the function in megabytes. The decorator should work with functions that do not take any arguments.
"""

import time
import resource
import functools

def timer_memory(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        start_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        result = func(*args, **kwargs)
        end_time = time.time()
        end_memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        print(f"Function '{func.__name__}' took {end_time - start_time:.6f} seconds to execute")
        print(f"Memory used by '{func.__name__}': {(end_memory - start_memory) / 1024.0:.2f} megabytes")
        return result
    return wrapper