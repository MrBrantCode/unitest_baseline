"""
QUESTION:
Implement a Python decorator named `log_function` that logs the name, arguments, and return value of a function when it's called. The decorator should use the `inspect` module to retrieve the function's signature.
"""

import inspect

def log_function(func):
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        print(f"Calling function: {func.__name__}")

        for name, value in bound_args.arguments.items():
            print(f"  {name} = {value}")

        result = func(*args, **kwargs)

        print(f"Return value: {result}")

        return result

    return wrapper