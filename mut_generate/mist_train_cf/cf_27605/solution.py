"""
QUESTION:
Implement the `measure_execution_time` decorator function, which takes a function as input and returns a new function that measures the execution time of the input function in milliseconds using the `process_time` function from the `time` module. The decorator should print the execution time after the function has completed its execution. The decorator function should have the following signature: `def measure_execution_time(func):`.
"""

from time import process_time

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = process_time()
        result = func(*args, **kwargs)
        end_time = process_time()
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        print(f"Execution time of {func.__name__}: {execution_time:.3f} milliseconds")
        return result
    return wrapper