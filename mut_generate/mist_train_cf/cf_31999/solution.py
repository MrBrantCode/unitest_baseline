"""
QUESTION:
Implement a decorator function named `base_decorator` that adds a new backend named "mock_backend" to the list of service discovery backends returned by the decorated function. The `base_decorator` function should accept the original function `func` as an argument, define the new backend, add it to the list of service discovery backends, and return the modified function. The decorated function should return the modified list of backends.
"""

def base_decorator(func):
    def wrapper(*args, **kwargs):
        new_backend = "mock_backend"
        modified_backends = func(*args, **kwargs) + [new_backend]
        return modified_backends
    return wrapper