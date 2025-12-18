"""
QUESTION:
Create a function `compare_dicts` that takes two dictionaries `dict1` and `dict2` as input and returns `True` if both dictionaries have the same keys and values, and `False` otherwise. The function should check for both key presence and value equality.
"""

def compare_dicts(dict1, dict2):
    if len(dict1) != len(dict2):
        return False
    
    for key in dict1:
        if key not in dict2 or dict1[key] != dict2[key]:
            return False
    
    return True