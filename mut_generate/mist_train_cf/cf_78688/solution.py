"""
QUESTION:
Implement a function `resolve_method_call` that simulates the process of resolving a method call in a prototype-based language. The function should take an object and a method name as input and return the object that contains the method, or None if the method is not found. The object's prototype is represented by its 'prototype' attribute. Assume that the method is a function that is an attribute of the object.
"""

def resolve_method_call(obj, method_name):
    """
    Simulates the process of resolving a method call in a prototype-based language.

    Args:
        obj (object): The object on which to resolve the method call.
        method_name (str): The name of the method to resolve.

    Returns:
        object: The object that contains the method, or None if the method is not found.
    """
    current_obj = obj
    while current_obj is not None:
        if hasattr(current_obj, method_name) and callable(getattr(current_obj, method_name)):
            return current_obj
        current_obj = getattr(current_obj, 'prototype', None)
    return None