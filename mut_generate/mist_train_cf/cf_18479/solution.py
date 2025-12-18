"""
QUESTION:
Create a function named `create_nested_dict` that takes two parameters: `keys_list` and `values_list`. `keys_list` is a list of strings, and `values_list` is a list of lists of integers. The function should return a nested dictionary where the keys are the strings from `keys_list`, and the values are dictionaries with keys as integers from `values_list` and values as the corresponding index of the integer in the inner lists of `values_list`. If there are duplicate keys in `keys_list`, the function should handle them accordingly.
"""

def create_nested_dict(keys_list, values_list):
    """
    Creates a nested dictionary from the given keys and values.

    Args:
        keys_list (list): A list of strings.
        values_list (list): A list of lists of integers.

    Returns:
        dict: A nested dictionary with keys from keys_list and values as dictionaries.
    """
    nested_dict = {}

    for i in range(len(keys_list)):
        key = keys_list[i]
        values = values_list[i]
        
        if key not in nested_dict:
            nested_dict[key] = {}
        
        for j in range(len(values)):
            value_key = values[j]
            
            if value_key not in nested_dict[key]:
                nested_dict[key][value_key] = []
            
            nested_dict[key][value_key].append(j)

    return nested_dict