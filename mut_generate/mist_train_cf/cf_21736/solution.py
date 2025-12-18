"""
QUESTION:
Write a function named `check_object_properties` that takes in two parameters: an object (a dictionary containing only strings and numbers) and a value to be searched for. The function should return `True` if all properties in the object are either strings or numbers and include the specified value, and `False` otherwise.
"""

def check_object_properties(obj, value):
    for key in obj:
        if obj[key] != value or not isinstance(obj[key], (str, int, float)):
            return False
    return True