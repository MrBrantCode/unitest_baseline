"""
QUESTION:
Write a function called `is_not_same_object` that checks if two objects are not the same object in Python. The function should return `True` if the objects are not the same, and `False` otherwise. The function should take two parameters, `obj1` and `obj2`, which are the objects to be compared.
"""

def is_not_same_object(obj1, obj2):
    return obj1 is not obj2