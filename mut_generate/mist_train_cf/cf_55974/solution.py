"""
QUESTION:
Write a function named `access_and_alter_nested_dict` that takes a dictionary `nested_dict` and a list of keys `keys` as input. The function should access the nested value corresponding to the given keys and update it with a new value `new_value`. The function should return the updated dictionary if the nested key exists; otherwise, it should return an error message.
"""

def access_and_alter_nested_dict(nested_dict, keys, new_value):
    """
    Access and alter a nested value in a dictionary.
    
    Args:
    nested_dict (dict): The dictionary containing the nested value.
    keys (list): A list of keys to access the nested value.
    new_value: The new value to be assigned to the nested key.
    
    Returns:
    dict: The updated dictionary if the nested key exists; otherwise, an error message.
    """
    current_dict = nested_dict
    for key in keys[:-1]:
        if key in current_dict:
            current_dict = current_dict[key]
        else:
            return "Error: Key does not exist."
    
    if keys[-1] in current_dict:
        current_dict[keys[-1]] = new_value
        return nested_dict
    else:
        return "Error: Key does not exist."