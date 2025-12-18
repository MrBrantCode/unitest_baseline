"""
QUESTION:
Implement the `sentry_monitor` decorator that takes an `error_stream` dictionary as an argument. The `error_stream` dictionary contains mappings for different error types to their corresponding error streams. The decorator should log the error to the appropriate error stream based on the type of error that occurs within the decorated function. The decorator should also re-raise the original exception.
"""

import functools

def sentry_monitor(error_stream):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                error_type = type(e).__name__
                if error_type in error_stream:
                    error_stream[error_type].log_error(e)
                else:
                    # Log to a default error stream or handle the error in a different way
                    pass
                raise
        return wrapper
    return decorator