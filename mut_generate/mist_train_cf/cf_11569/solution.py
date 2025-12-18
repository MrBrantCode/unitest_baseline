"""
QUESTION:
Implement a function called `is_integer(variable)` that determines whether a given variable is an integer or not, without using any built-in functions or libraries for type checking. The function should handle edge cases such as strings and floats that represent integers, booleans that represent integers, and lists or dictionaries that contain integers. The function should be efficient and able to handle large inputs without consuming excessive memory or taking too long to execute.
"""

def is_integer(variable):
    # Check if the variable is of type int
    if type(variable) == int:
        return True
    
    # Check if the variable is a string that represents an integer
    if type(variable) == str:
        try:
            int(variable)
            return True
        except ValueError:
            return False
    
    # Check if the variable is a float that represents an integer
    if type(variable) == float:
        if variable.is_integer():
            return True
    
    # Check if the variable is a boolean that represents an integer
    if type(variable) == bool:
        if variable in (0, 1):
            return True
    
    # Check if the variable is a list or dictionary that contains integers
    if type(variable) in (list, dict):
        for value in variable.values() if type(variable) == dict else variable:
            if not is_integer(value):
                return False
        return True
    
    return False