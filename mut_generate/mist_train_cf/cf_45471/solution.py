"""
QUESTION:
Create a function `remove_empty_values` that takes a dictionary as input and returns a new dictionary with all key-value pairs where the value is considered empty removed. In Python, empty values are those that are equivalent to `False` in a boolean context, including but not limited to `None`, `''`, `0`, `False`, `[]`, `{}`, etc. The function should not modify the original dictionary.
"""

def remove_empty_values(my_dict):
    return {k: v for k, v in my_dict.items() if v}

# alternative version
def remove_empty_values(my_dict):
    return {k: v for k, v in my_dict.items() if v is not None and v != ''}