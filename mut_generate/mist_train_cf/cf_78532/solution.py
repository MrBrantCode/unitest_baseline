"""
QUESTION:
Write a function called `select_variable` that determines the appropriate data type and scope for a given variable in a program. The function should take two parameters: `variable_name` and `variable_value`. The function should return a tuple containing the recommended data type and scope for the variable. 

The function should consider the range of possible values, memory size, and desired level of precision when selecting the data type. It should also determine the scope based on the intended usage within the program, with a preference for local scope unless the variable needs to be accessed and manipulated by multiple functions.
"""

def select_variable(variable_name, variable_value):
    """
    This function determines the appropriate data type and scope for a given variable in a program.

    Parameters:
    variable_name (str): The name of the variable.
    variable_value: The value of the variable.

    Returns:
    tuple: A tuple containing the recommended data type and scope for the variable.
    """

    # Determine the data type based on the variable's value
    if isinstance(variable_value, int):
        data_type = "int"
    elif isinstance(variable_value, float):
        data_type = "float"
    elif isinstance(variable_value, str):
        data_type = "str"
    else:
        data_type = "unknown"

    # Determine the scope based on the variable's name (for simplicity, assume local scope unless the name starts with 'global_')
    if variable_name.startswith('global_'):
        scope = "global"
    else:
        scope = "local"

    return data_type, scope