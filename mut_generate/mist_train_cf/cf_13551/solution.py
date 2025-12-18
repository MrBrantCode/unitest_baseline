"""
QUESTION:
Create a function called `is_immutable` that takes an object as input and returns `True` if the object is immutable and `False` otherwise. The function should work with built-in Python types. Assume the input will always be a single object, not a collection of objects.
"""

def is_immutable(obj):
    """
    This function checks if an object is immutable or not.
    
    Args:
    obj: The object to be checked for immutability.
    
    Returns:
    bool: True if the object is immutable, False otherwise.
    """
    immutable_types = (int, float, str, tuple, frozenset, bytes)
    return isinstance(obj, immutable_types)