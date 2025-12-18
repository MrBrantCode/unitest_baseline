"""
QUESTION:
Create a function `simulate_retry` that takes in four parameters: `func`, `wait_exponential_multiplier`, `wait_exponential_max`, and `retry_on_exception`. The function should implement a retry mechanism with exponentially increasing wait times between retries. The wait time starts at `wait_exponential_multiplier` milliseconds and doubles with each retry, up to a maximum of `wait_exponential_max` milliseconds. The retry mechanism should only trigger if the `func` raises an exception and `retry_on_exception` returns `True` for that exception. If `func` does not raise an exception or `retry_on_exception` returns `False`, the function should return the result of `func`.
"""

import time

def simulate_retry(func, wait_exponential_multiplier, wait_exponential_max, retry_on_exception):
    def retry_decorator(*args, **kwargs):
        current_wait_time = wait_exponential_multiplier
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if retry_on_exception(e):
                    time.sleep(current_wait_time / 1000)  # Convert milliseconds to seconds
                    current_wait_time = min(2 * current_wait_time, wait_exponential_max)
                else:
                    raise
    return retry_decorator