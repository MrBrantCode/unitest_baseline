"""
QUESTION:
Write a Python function `ensure_decorator` that takes two arguments: `max_attempts` (an integer) and `exceptions` (a tuple of Exception classes). The function should return a decorator that catches the specified exceptions, retries a given function up to `max_attempts` times, and re-raises the exception if the function still fails after `max_attempts`.
"""

def ensure_decorator(max_attempts, exceptions):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise e
        return wrapper
    return decorator