"""
QUESTION:
Write a function `dict_diff` that compares two dictionaries (`obj1` and `obj2`) and returns a dictionary containing their differences, considering case sensitivity and nested properties. The function should return a dictionary where the keys are the differing keys in `obj1` and `obj2`, and the values are tuples containing the corresponding values in `obj1` and `obj2`. If a key is present in only one of the dictionaries, the tuple should contain the value from the dictionary that has the key and `None` for the other dictionary. If the values are dictionaries themselves, the function should recursively call itself to find the nested differences.
"""

def dict_diff(obj1, obj2):
    """
    This function compares two dictionaries and returns a dictionary containing their differences.
    
    Args:
        obj1 (dict): The first dictionary to compare.
        obj2 (dict): The second dictionary to compare.
    
    Returns:
        dict: A dictionary containing the differences between obj1 and obj2.
    """
    diff = {}
    for key in obj1.keys() | obj2.keys():
        if key in obj1 and key in obj2:
            if isinstance(obj1[key], dict) and isinstance(obj2[key], dict):
                nested_diff = dict_diff(obj1[key], obj2[key])
                if nested_diff:
                    diff[key] = nested_diff
            elif obj1[key] != obj2[key]:
                diff[key] = (obj1[key], obj2[key])
        elif key in obj1:
            diff[key] = (obj1[key], None)
        elif key in obj2:
            diff[key] = (None, obj2[key])

    return diff