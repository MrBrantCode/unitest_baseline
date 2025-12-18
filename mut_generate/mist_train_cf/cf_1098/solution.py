"""
QUESTION:
Create a function named `create_nested_dict` that takes two parameters: a list of keys and a list of values. The keys list may contain nested lists, and the function should construct a nested dictionary where each key is assigned the corresponding value. The function should have a time complexity of O(n^3) and a space complexity of O(n^2). If a key is a nested list, the value should be assigned to the innermost key in the list, with the key "value" used as a placeholder if the innermost key is a list.
"""

def entrance(keys, values):
    """
    Construct a nested dictionary from a list of keys and a list of values.
    
    Args:
        keys (list): A list of keys, which may contain nested lists.
        values (list): A list of values to be assigned to the corresponding keys.
    
    Returns:
        dict: A nested dictionary where each key is assigned the corresponding value.
    """
    nested_dict = {}
    def add_to_nested_dict(nested_dict, key, value):
        if isinstance(key, list):
            if len(key) == 1:
                nested_dict[key[0]] = {'value': value}
            else:
                nested_dict[key[0]] = add_to_nested_dict(nested_dict.get(key[0], {}), key[1:], value)
        else:
            nested_dict[key] = value
        return nested_dict

    for i in range(len(keys)):
        nested_dict = add_to_nested_dict(nested_dict, keys[i], values[i])
    return nested_dict