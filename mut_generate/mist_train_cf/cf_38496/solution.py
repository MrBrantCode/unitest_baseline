"""
QUESTION:
Create a function `closure_generator` that takes an object as input and returns a closure. The returned closure should take an optional argument and have the following behavior: when called without an argument, it returns the current state of the object; when called with an argument, it updates the state of the object to the provided argument and returns the updated object.
"""

def closure_generator(obj):
    def closure(new_obj=None):
        nonlocal obj
        if new_obj is not None:
            obj = new_obj
        return obj
    return closure