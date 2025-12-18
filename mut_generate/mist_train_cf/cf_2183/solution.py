"""
QUESTION:
Create a function named `check_type_and_length` that takes two variables as input and returns `True` if they have the same type. If the variables are lists, the function should also return `True` if they have the same length and the same type and length/keys for all nested elements. If the variables are dictionaries, the function should also return `True` if they have the same keys and the same type and length/keys for all nested elements. The function should handle nested data structures.
"""

def check_type_and_length(var1, var2):
    if type(var1) != type(var2):
        return False

    if isinstance(var1, list):
        if len(var1) != len(var2):
            return False
        for i in range(len(var1)):
            if not check_type_and_length(var1[i], var2[i]):
                return False

    elif isinstance(var1, dict):
        if set(var1.keys()) != set(var2.keys()):
            return False
        for key in var1.keys():
            if not check_type_and_length(var1[key], var2[key]):
                return False

    return True