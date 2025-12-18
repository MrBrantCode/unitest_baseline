"""
QUESTION:
Implement a decorator `print_calls` that takes a function as input and returns a new function. When the decorated function is called, it should print the name of the function and its arguments, then execute the function and return its result. The decorator should work with functions that take any number of positional and keyword arguments.
"""

def print_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper