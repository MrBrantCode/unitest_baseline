"""
QUESTION:
Create a function `check_type_and_length` that takes two variables as input and returns `True` if they have the same type. If both variables are lists, the function should also return `True` only if they have the same length.
"""

def check_type_and_length(var1, var2):
    if type(var1) != type(var2):
        return False
    
    if isinstance(var1, list) and isinstance(var2, list):
        if len(var1) != len(var2):
            return False
    
    return True