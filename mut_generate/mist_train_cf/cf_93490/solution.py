"""
QUESTION:
Implement a function `find_value(env, variable)` that retrieves the value of a variable from a given environment `env` (a nested dictionary) based on the `variable` string, which may contain dot notation for nested keys. The function should return `None` if the variable does not exist, the value is not an integer, or if the variable is not a string.
"""

def find_value(env, variable):
    """
    Retrieves the value of a variable from a given environment (a nested dictionary) 
    based on the variable string, which may contain dot notation for nested keys.
    
    Args:
        env (dict): The environment dictionary.
        variable (str): The variable string.

    Returns:
        int or None: The value of the variable if it exists and is an integer, otherwise None.
    """

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