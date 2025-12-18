"""
QUESTION:
Create a function `create_new_dict` that takes a nested dictionary as input and returns a new dictionary. The keys of the new dictionary should be the values of the "name" key from the nested dictionary, and the values should be the corresponding values of the "needed_value" key. Assume that the input dictionary is not empty and that each inner dictionary contains the "name" and "needed_value" keys.
"""

def create_new_dict(nested_dict):
    """
    This function creates a new dictionary from a nested dictionary.
    The keys of the new dictionary are the values of the "name" key from the nested dictionary,
    and the values are the corresponding values of the "needed_value" key.

    Args:
        nested_dict (dict): A dictionary containing nested dictionaries with "name" and "needed_value" keys.

    Returns:
        dict: A new dictionary with "name" values as keys and "needed_value" values as values.
    """
    return {v['name']: v['needed_value'] for k, v in nested_dict.items()}