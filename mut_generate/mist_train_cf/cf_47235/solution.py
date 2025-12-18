"""
QUESTION:
Implement a function `check_types` that simulates static typing by checking the types of two variables and comparing them. The function should take two parameters, `var1` and `var2`, and their corresponding types `type1` and `type2`, and return `True` if both variables match their respective types, and `False` otherwise. Assume that the variables and types are passed as strings, and consider the basic types such as 'int', 'float', and 'str'.
"""

def check_types(var1, var2, type1, type2):
    """
    Simulates static typing by checking the types of two variables and comparing them.

    Args:
    var1 (str): The first variable.
    var2 (str): The second variable.
    type1 (str): The type of the first variable.
    type2 (str): The type of the second variable.

    Returns:
    bool: True if both variables match their respective types, False otherwise.
    """
    type_mapping = {
        'int': int,
        'float': float,
        'str': str
    }
    
    try:
        var1_type = type_mapping[type1]
        var2_type = type_mapping[type2]
        
        return isinstance(var1, var1_type) and isinstance(var2, var2_type)
    except KeyError:
        return False