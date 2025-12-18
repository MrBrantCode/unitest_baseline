"""
QUESTION:
Create a function `check_type_and_length(var1, var2)` that checks if two variables `var1` and `var2` have the same type. If `var1` and `var2` are lists, the function should also check if they have the same length. If `var1` and `var2` are dictionaries, the function should also check if they have the same keys. The function should also handle nested data structures, where lists or dictionaries may be nested within each other, and perform the same type and length checks for all nested elements.
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