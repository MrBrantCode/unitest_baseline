"""
QUESTION:
Create a function `check_property_value` that takes in two parameters: an object (dictionary) and a value. The function should return `True` if all properties in the object have the same value, and `False` otherwise.
"""

def check_property_value(obj, value):
    """
    This function checks if all properties in the object have the same value.

    Args:
    obj (dict): The dictionary object to check.
    value: The value to compare with.

    Returns:
    bool: True if all properties have the same value, False otherwise.
    """
    return all(obj[prop] == value for prop in obj)