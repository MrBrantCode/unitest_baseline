"""
QUESTION:
Implement a function `match(obj, *args)` that takes an object and a variable number of arguments, where the last argument is a dictionary of values to match, and the preceding arguments are the paths to be checked within the object. The function should return True if all the paths exist in the object and their corresponding values match the provided dictionary; otherwise, it should return False.
"""

def match(obj, *args):
    *paths, values = args
    current_obj = obj
    for path in paths:
        if isinstance(current_obj, dict) and path in current_obj:
            current_obj = current_obj[path]
        else:
            return False
    for key, value in values.items():
        if key not in current_obj or current_obj[key] != value:
            return False
    return True