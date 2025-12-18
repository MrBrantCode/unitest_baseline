"""
QUESTION:
Implement a Python decorator named `reschedule_counter` that takes a function `func` as input and returns a wrapper function. The `reschedule_counter` decorator should maintain a count of how many times the wrapped function `func` is called and raise a custom exception message if `func` fails during execution. The decorator should be able to wrap any given function.
"""

def entrance(func):
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, 'reschedule_count'):
            wrapper.reschedule_count = 0
        try:
            func(*args, **kwargs)
        except Exception as e:
            raise Exception(f'Failed execution in function: {func.__name__!r}') from e
        wrapper.reschedule_count += 1
    return wrapper