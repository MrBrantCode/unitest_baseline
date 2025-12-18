"""
QUESTION:
Write a function `check_variable_type` that takes a variable as input and returns a string describing the type of the variable. If the variable is a list, the function should also return the number of elements in the list. The function should only return the type information and the number of elements if the variable is a list; otherwise, it should only return the type information.
"""

def check_variable_type(var):
    var_type = type(var).__name__
    if isinstance(var, list):
        return f"Variable is of type {var_type} and has {len(var)} elements."
    else:
        return f"Variable is of type {var_type}"