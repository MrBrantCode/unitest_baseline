"""
QUESTION:
Write a function `is_immutable(obj)` that takes an object as input and returns `True` if the object is immutable and `False` otherwise. The function should work for built-in Python types.
"""

def is_immutable(obj):
    """
    Checks if an object is immutable in Python.
    
    Args:
    obj: The object to check for immutability.
    
    Returns:
    True if the object is immutable, False otherwise.
    """
    
    # Check the type of the object to determine its immutability
    immutable_types = (int, float, complex, str, tuple, frozenset, bytes)
    return isinstance(obj, immutable_types)