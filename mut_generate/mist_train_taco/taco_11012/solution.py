"""
QUESTION:
Each test case will generate a variable whose value is 777. Find the name of the variable.
"""

def find_variable_with_value(value):
    """
    Finds the name of the variable in the global scope that holds the specified value.

    Parameters:
    - value: The value to search for in the global variables.

    Returns:
    - The name of the variable that holds the specified value, or None if no such variable exists.
    """
    return next((k for k, v in globals().items() if v == value), None)