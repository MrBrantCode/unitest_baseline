"""
QUESTION:
Create a function `identify_variable_type` that determines the type of a given variable. The function should identify the variable as an integer, float, or string. The input value will be a single variable.
"""

def identify_variable_type(var):
    """
    This function determines the type of a given variable.
    
    Parameters:
    var (any): The variable to check.
    
    Returns:
    str: The type of variable.
    """
    if isinstance(var, int):
        return "integer"
    elif isinstance(var, float):
        return "float"
    elif isinstance(var, str):
        return "string"
    else:
        return "unknown"