"""
QUESTION:
Create a Python decorator function named `log_arguments_and_return` that logs the arguments passed to and the return value of the decorated function. The decorator should work with any function and any number of arguments, including positional and keyword arguments. The logged arguments should include both positional and keyword arguments. The decorator should return the result of the original function.
"""

def log_arguments_and_return(func):
    """
    Decorator to log the arguments and return value of a function
    :param func: The function to be decorated
    :return: The decorated function
    """
    def wrapper(*args, **kwargs):
        # Log the arguments
        print(f"Arguments: {args}, {kwargs}")
        # Call the original function
        result = func(*args, **kwargs)
        # Log the return value
        print(f"Return value: {result}")
        return result
    return wrapper