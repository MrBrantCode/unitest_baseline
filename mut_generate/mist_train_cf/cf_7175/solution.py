"""
QUESTION:
Create a function `check_object_properties` that takes in two parameters: `obj` and `value`. The function should return `True` if all properties in the object `obj` include the `value` and are of type string, number, array, or nested object, and `False` otherwise. The function should recursively check nested objects.
"""

def check_object_properties(obj, value):
    for prop in obj:
        prop_value = obj[prop]
        if prop_value != value:
            if not (isinstance(prop_value, str) or isinstance(prop_value, int) or isinstance(prop_value, list) or isinstance(prop_value, dict)):
                return False
            elif isinstance(prop_value, dict):
                if not check_object_properties(prop_value, value):
                    return False
    return True