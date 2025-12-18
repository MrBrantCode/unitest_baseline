"""
QUESTION:
Create a function named `check_variables` that takes two parameters, `var1` and `var2`. The function should return `True` if `var1` and `var2` have the same type. If they are lists, they must also have the same length. If they are dictionaries, they must also have the same keys. The function should work for lists and dictionaries, as well as any other types.
"""

def check_variables(var1, var2):
    # Check if the variables have the same type
    if type(var1) != type(var2):
        return False
    
    # If the variables are lists, check if they have the same length
    if isinstance(var1, list) and isinstance(var2, list):
        if len(var1) != len(var2):
            return False
    
    # If the variables are dictionaries, check if they have the same keys
    if isinstance(var1, dict) and isinstance(var2, dict):
        if set(var1.keys()) != set(var2.keys()):
            return False
    
    # If none of the above conditions are met, return True
    return True