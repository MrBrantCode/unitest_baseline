"""
QUESTION:
Write a function `check_same_type(lst)` that checks if all items in a list are of the same data type. The function should return True if all items are of the same type and False otherwise. The list can contain any valid Python data type, including nested lists and dictionaries. The function should have optimal time complexity and should not use built-in functions or methods that directly determine the data type of an object (e.g., type() or isinstance()).
"""

def check_same_type(lst):
    if len(lst) < 2:
        return True

    first_type = get_data_type(lst[0])
    for item in lst[1:]:
        if first_type != get_data_type(item):
            return False

    return True


def get_data_type(item):
    if isinstance(item, list):
        return "list"
    elif isinstance(item, dict):
        return "dict"
    elif isinstance(item, str):
        return "str"
    elif isinstance(item, int):
        return "int"
    elif isinstance(item, float):
        return "float"
    elif isinstance(item, bool):
        return "bool"
    else:
        return "other"