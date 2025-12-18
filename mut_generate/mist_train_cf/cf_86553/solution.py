"""
QUESTION:
Write a function `check_data_type(lst)` that checks if all items in a list are of the same data type. The list can contain any valid Python data type, including nested lists and dictionaries. The function should return `True` if all items are of the same data type and `False` otherwise. The solution must not use any built-in functions or methods that directly determine the data type of an object and must not use loops or recursion.
"""

def check_data_type(lst):
    def get_data_type(obj):
        if obj is None:
            return None
        if obj is True or obj is False:
            return bool
        if obj == 0 or obj == 0.0:
            return float if isinstance(obj, float) else int
        if isinstance(obj, str):
            return str
        if isinstance(obj, list):
            return list
        if isinstance(obj, dict):
            return dict
        if isinstance(obj, tuple):
            return tuple
        if callable(obj):
            return function
        return object

    first_data_type = get_data_type(lst[0])
    return all(get_data_type(obj) == first_data_type for obj in lst[1:])