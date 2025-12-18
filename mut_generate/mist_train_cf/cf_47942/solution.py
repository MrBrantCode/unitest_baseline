"""
QUESTION:
Implement a class `MyClass` that inherits from two classes, `Base` and `Mixin`, where `Base` has an attribute `access_level` and `Mixin` has a method `extra_functionality`. `MyClass` should have a method `perform_operation` that is decorated with a function `restricted_access` which checks if `access_level` is "restricted" and prevents the operation if true. The `restricted_access` function should be a decorator that takes in a function and returns a wrapper function. The `access_level` attribute should be set to "open" by default and can be changed to "restricted" to prevent the operation.
"""

def restricted_access(decorated_function):
    def wrapper(obj, *args, **kwargs):
        if obj.access_level == "restricted":
            print("Restricted access. Operation not allowed.")
        else:
            decorated_function(obj, *args, **kwargs)
    return wrapper

class Base:
    def __init__(self):
        self.access_level = "open"

class Mixin:
    def extra_functionality(self):
        print("Mixin provides extra functionality...")

class MyClass(Base, Mixin):
    def __init__(self):
        super().__init__()

    @restricted_access
    def perform_operation(self):
        print("Performing operation in MyClass...")