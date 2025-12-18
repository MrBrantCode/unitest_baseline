"""
QUESTION:
Create a function, `is_true_or_false`, that takes an input value of any data type and returns `True` if the value is equivalent to 'true' and `False` otherwise. The function should handle inconsistent data types, including different numeric types and mixed case strings, and should be able to differentiate between boolean values and strings containing 'true' or 'false'. The function should return `False` for invalid or unknown inputs.
"""

def is_true_or_false(value):
    # If the input can be casted to boolean, use str to differentiate between boolean values and strings
    if isinstance(value, bool):
        return value
    elif isinstance(value, str):
        if value.lower() == 'true':
            return True
        elif value.lower() == 'false':
            return False
    elif isinstance(value, (int, float)):
        return bool(value)
    # Return False for all other instances as they are not 'true' or 'false'
    return False


def is_true_or_false(value):
    try:
        return {"0": False, "1": True, "true": True, "false": False}[str(value).lower()]
    except (ValueError, TypeError, KeyError):
        return False