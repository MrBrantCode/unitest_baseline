"""
QUESTION:
Write a function `check_object_properties` that takes in two parameters: an object `obj` and a value `val`. The function should check if all properties of the object `obj` are either strings or numbers and include the specified value `val`. If any property does not meet these conditions, the function should return `False`; otherwise, it should return `True`. The object `obj` is only allowed to contain strings and numbers as property values.
"""

def check_object_properties(obj, val):
    """Checks if all properties of the object are either strings or numbers and include the specified value."""
    for key in obj:
        if obj[key] != val or not isinstance(obj[key], (str, int, float)):
            return False
    return True