"""
QUESTION:
Implement the `serialize` method in the `Serializer` class to handle the serialization of different data types. The method should take an object of type `Any` as input and return a dictionary. The method should handle the serialization of simple types (int, float, str, etc.) and any other data types not covered by the existing methods. The serialization should be done recursively for nested data structures. The existing `serialize_sequence` and `serialize_mapping` methods can be used to handle sequences and mappings, respectively.
"""

from collections.abc import Mapping, Sequence
from typing import Any

def serialize(obj: Any) -> dict:
    if isinstance(obj, Sequence) and not isinstance(obj, str):
        return [serialize(item) for item in obj]
    elif isinstance(obj, Mapping):
        return {k: serialize(v) for k, v in obj.items()}
    else:
        if isinstance(obj, (int, float, str, bool, type(None))):
            return obj
        elif isinstance(obj, type):
            return obj.__name__
        else:
            return str(obj)