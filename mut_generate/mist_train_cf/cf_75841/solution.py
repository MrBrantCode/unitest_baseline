"""
QUESTION:
Implement a Python function `measure_runtime(func)` that measures the wall clock runtime of a given function `func` in fractional seconds. The function should return the runtime as a float value. Note that this function will not account for actual CPU time spent by system processes and other programs running concurrently.
"""

import time

def measure_runtime(func):
    start_time = time.perf_counter()
    func()
    end_time = time.perf_counter()
    return end_time - start_time