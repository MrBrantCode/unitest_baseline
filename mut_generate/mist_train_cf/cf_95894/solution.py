"""
QUESTION:
Create a class named `CustomContextManager` that serves as a context manager with the following properties:

* The class should implement the `__enter__` and `__exit__` methods to ensure resources are properly acquired and released.
* It should support nested context managers, handling multiple levels of nesting and acquiring/releasing resources in the correct order.
* The class should track the total number of times it has been entered and exited, accessible through a method.
* The class should allow for a custom callback function to be executed upon exit, receiving the total enter and exit counts as arguments.

The class should take an optional `custom_callback` parameter in its constructor. The `__exit__` method should propagate exceptions if any occur within the context block.
"""

def custom_context_manager(custom_callback=None):
    enter_count = 0
    exit_count = 0

    def acquire_resource():
        nonlocal enter_count
        enter_count += 1

    def release_resource(exc_type, exc_val, exc_tb):
        nonlocal exit_count
        exit_count += 1
        if custom_callback is not None:
            custom_callback(enter_count, exit_count)
        return False

    return acquire_resource, release_resource