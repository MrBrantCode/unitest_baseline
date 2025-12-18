"""
QUESTION:
Create a decorator named `error_handler` that takes a function as an argument and returns a new function. The new function should handle any error raised by the original function and re-raise it with a custom error message that includes the original error message and the name of the function where the error occurred. The decorator should be able to handle any type of exception.
"""

def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise type(e)(f"Error in function {func.__name__}: {str(e)}")
    return wrapper