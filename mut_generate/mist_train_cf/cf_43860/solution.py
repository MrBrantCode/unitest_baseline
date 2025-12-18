"""
QUESTION:
Create a decorator named `log_decorator` that logs the execution time, number of invocations, and any exceptions raised during the execution of a function. The decorator should reset the invocation count after every 10 invocations. The decorator should be generic and work with any function.
"""

import time
import functools

def log_decorator(func):
    # Initialize metadata
    func._invocations = 0
    func._exceptions = 0

    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Record start time
        start_time = time.perf_counter()

        # Execute function
        try:
            func._invocations += 1
            result = func(*args, **kwargs)
        except Exception as e:
            func._exceptions += 1
            print(f'Exception Occurred on {func.__name__!r}: {e}')
            return None
        else:
            # Record end time
            end_time = time.perf_counter()

            # Log execution info
            print(f'Executed {func.__name__!r} in {(end_time-start_time):.4f} secs.')
            print(f'Invocation of {func.__name__!r}: #{func._invocations}')
            if func._exceptions > 0:
                print(f'Exceptions during {func.__name__!r}: {func._exceptions}')

            # Reset counts every 10 invocations
            if func._invocations >= 10:
                func._invocations = 0
                func._exceptions = 0

            return result

    return wrapper_decorator