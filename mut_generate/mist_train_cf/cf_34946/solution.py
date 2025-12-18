"""
QUESTION:
Implement a function `convert_bool(x)` that converts a given input `x` to a boolean value. The function should return the input `x` as is if it is already a boolean. If `x` is a string, it should be converted to a boolean based on the following rules:
- 'true', 't', '1' (case-insensitive) are considered True
- 'false', 'f', '0' (case-insensitive) are considered False
- Any other input type or string representation should return None.
"""

def convert_bool(x):
    if isinstance(x, bool):  
        return x
    elif isinstance(x, str):  
        if x.lower() in ('true', 't', '1'):  
            return True
        elif x.lower() in ('false', 'f', '0'):  
            return False
    return None  