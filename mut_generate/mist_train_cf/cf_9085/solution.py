"""
QUESTION:
Write a function `convert_nested_list_to_dict` that takes a nested list as input, where each sublist contains a key-value pair, and the value can be another dictionary or a list of key-value pairs. The function should return a nested dictionary where each key is the first element of a sublist, and the corresponding value is the second element of the sublist. If the value is a list, it should be recursively converted to a dictionary. If the value is another dictionary, it should be left unchanged.
"""

def convert_nested_list_to_dict(nested_list):
    """
    This function takes a nested list as input, where each sublist contains a key-value pair, 
    and the value can be another dictionary or a list of key-value pairs. It returns a 
    nested dictionary where each key is the first element of a sublist, and the corresponding 
    value is the second element of the sublist. If the value is a list, it is recursively 
    converted to a dictionary. If the value is another dictionary, it is left unchanged.

    Args:
        nested_list (list): A nested list of key-value pairs.

    Returns:
        dict: A nested dictionary where each key is the first element of a sublist, 
              and the corresponding value is the second element of the sublist.
    """
    nested_dict = {}
    for item in nested_list:
        key = item[0]
        value = item[1]
        if isinstance(value, list):
            nested_dict[key] = convert_nested_list_to_dict(value)
        else:
            nested_dict[key] = value
    return nested_dict