"""
QUESTION:
Implement a custom data structure named `OrderedDefaultDict` that maintains the order of key insertion and automatically assigns a default value to a key not present in the dictionary. The `OrderedDefaultDict` class should take a `default_factory` parameter in its constructor, which is a function that returns the default value to be assigned to a key when it is not present. If no `default_factory` is provided, attempting to access a non-existent key should raise a `KeyError`.
"""

from collections import OrderedDict

def ordered_default_dict(default_factory=None, *args, **kwargs):
    if default_factory is None:
        return OrderedDict(*args, **kwargs)
    else:
        ordered_dict = OrderedDict(*args, **kwargs)
        def __missing__(key):
            value = default_factory()
            ordered_dict[key] = value
            return value
        ordered_dict.__missing__ = __missing__
        return ordered_dict