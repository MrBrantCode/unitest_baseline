"""
QUESTION:
Implement a Python decorator `interceptor` that takes three optional keyword arguments: `before`, `after`, and `onSuccess`. The `before` function should be executed before the decorated function is called, the `after` function should be executed after the decorated function is called, and the `onSuccess` function should be executed if the decorated function completes successfully, with the result of the decorated function and the time elapsed during its execution passed as arguments. The decorator should also handle error scenarios by executing an `onError` function, which is assumed to be defined, if an exception occurs during the decorated function's execution.
"""

import time
from functools import wraps

def entance(before=None, after=None, onSuccess=None):
    def decorator(func):
        @wraps(func)
        def call(*args, **kwargs):
            try:
                if before is not None:
                    before()
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                time_elapsed = (end_time - start_time) * 1000
                if after is not None:
                    after()
                if onSuccess is not None:
                    onSuccess(result, f'time elapsed => {time_elapsed}')
                return result
            except Exception as ex:
                if 'onError' in globals():
                    onError(ex)
        return call
    return decorator