"""
QUESTION:
Implement a Python decorator named `selection` that takes a single argument `condition`, a function that returns a boolean value indicating whether the decorated function should be executed. The `selection` decorator should apply the decorated function if `condition` returns `True` and apply a different function `deselection` if `condition` returns `False`. The `deselection` function is predefined and does not take any arguments. The decorated function and `condition` function take the same arguments.
"""

def selection(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                return deselection()
        return wrapper
    return decorator

def deselection():
    return "Deselection function executed"