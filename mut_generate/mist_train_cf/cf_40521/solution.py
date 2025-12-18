"""
QUESTION:
Create a decorator called `entry_exit` that logs the entry and exit of a function. The decorator should print a message when the function is entered and exited, along with the function name and its arguments, and preserve the original function's return value. The entry message should be in the format "Entering <function_name> with arguments <arguments>" and the exit message should be in the format "Exiting <function_name> with return value <return_value>".
"""

def entry_exit(func):
    def wrapper(*args, **kwargs):
        print(f"Entering {func.__name__} with arguments {args}")
        result = func(*args, **kwargs)
        print(f"Exiting {func.__name__} with return value {result}")
        return result
    return wrapper