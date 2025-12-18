"""
QUESTION:
Implement a function `check_membership` that takes in two parameters: a collection (such as a list, tuple, or string) and a value. The function should return `True` if the value is present in the collection and `False` otherwise. The function should be able to handle different types of collections and values, but it should not be designed to work with NumPy arrays or similar objects.
"""

def check_membership(collection, value):
    """
    Checks if a value is present in a given collection.

    Args:
        collection (list, tuple, string): A collection of values.
        value: The value to be searched in the collection.

    Returns:
        bool: True if the value is present in the collection, False otherwise.
    """
    return value in collection