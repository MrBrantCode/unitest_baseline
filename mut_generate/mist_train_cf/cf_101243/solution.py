"""
QUESTION:
Create a function named `serialize_with_pickle` that uses the Python Pickle library to serialize and deserialize a given object. The object can be of any type, including basic data types, lists, tuples, dictionaries, sets, classes, functions, modules, and custom objects. The function should handle nested objects with complex data structures.
"""

import pickle

def serialize_with_pickle(obj):
    """
    This function uses the Python Pickle library to serialize and deserialize a given object.

    Args:
    obj (object): The object to be serialized. The object can be of any type, including basic data types, lists, tuples, dictionaries, sets, classes, functions, modules, and custom objects.

    Returns:
    bytes: The serialized object in bytes format.
    """
    return pickle.dumps(obj)

def deserialize_with_pickle(serialized_obj):
    """
    This function deserializes a given object that was previously serialized using the Python Pickle library.

    Args:
    serialized_obj (bytes): The serialized object in bytes format.

    Returns:
    object: The deserialized object.
    """
    return pickle.loads(serialized_obj)