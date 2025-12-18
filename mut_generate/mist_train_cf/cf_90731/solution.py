"""
QUESTION:
Write a function `convert_nested_list_to_dict` to convert a nested list into a nested dictionary. The input list contains sublists where the first element of each sublist is a key and the second element is either a dictionary or another list that needs to be converted into a dictionary. The function should recursively handle nested dictionaries and return the resulting nested dictionary.
"""

def convert_nested_list_to_dict(nested_list):
    """
    Convert a nested list into a nested dictionary.

    Args:
        nested_list (list): A list containing sublists where the first element of each sublist is a key
            and the second element is either a dictionary or another list that needs to be converted into a dictionary.

    Returns:
        dict: The resulting nested dictionary.
    """
    nested_dict = {}
    for item in nested_list:
        key = item[0]
        value = item[1]
        if isinstance(value, list):
            nested_dict[key] = convert_nested_list_to_dict(value)
        elif isinstance(value, dict):
            nested_dict[key] = value
        else:
            nested_dict[key] = value
    return nested_dict