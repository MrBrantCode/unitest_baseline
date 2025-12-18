"""
QUESTION:
Write a Python function named `assign_variable` that demonstrates variable assignment and usage in a program, considering the variable can store different data types and can be reassigned. The function should take two arguments: the initial variable name and its initial value. It should return a string that includes the variable name, its initial value, and its reassigned value. The initial value can be of any data type (e.g., integer, float, string). The reassigned value should be of a different data type than the initial value.
"""

def assign_variable(variable_name, initial_value):
    """
    This function demonstrates variable assignment and usage in a program.
    
    Args:
        variable_name (str): The initial variable name.
        initial_value: The initial value of the variable. Can be of any data type.
    
    Returns:
        str: A string that includes the variable name, its initial value, and its reassigned value.
    """
    
    # Assign the initial value to the variable
    variable = initial_value
    
    # Reassign the variable with a different data type
    if isinstance(initial_value, int):
        variable = "String value"
    elif isinstance(initial_value, str):
        variable = 10
    elif isinstance(initial_value, float):
        variable = "Float value"
    
    # Return a string with the variable name, initial value, and reassigned value
    return f"Variable: {variable_name}, Initial Value: {initial_value}, Reassigned Value: {variable}"