"""
QUESTION:
Write a function `find_value(env, variable)` that retrieves the value of a given variable from a nested dictionary environment. The function should handle potential errors, including non-existent keys, non-string variables, and non-integer values. If an error occurs, the function should return `None`. The variable can contain dot notation to represent nested dictionaries.
"""

def find_value(env, variable):
    default_value = None
    
    if not isinstance(variable, str):
        return default_value
    
    keys = variable.split('.')
    current_dict = env
    
    try:
        for key in keys:
            current_dict = current_dict[key]
    except (KeyError, TypeError):
        return default_value
    
    if not isinstance(current_dict, int):
        return default_value
    
    return current_dict