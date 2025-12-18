"""
QUESTION:
Write a function `monadic_function` that takes a single argument, either a value or a collection of values, and returns a result that is also a value or a collection of values.
"""

def monadic_function(arg):
    if isinstance(arg, (list, tuple)):
        return [item * 2 for item in arg]
    else:
        return arg * 2