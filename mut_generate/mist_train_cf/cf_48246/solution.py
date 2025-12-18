"""
QUESTION:
Create a function called `merge_lists_to_dict` that takes three lists as input: `keys_list`, `values_list`, and `sub_values_list`. The function should merge these lists into a single dictionary structure, where the elements of `keys_list` are the keys, the elements of `values_list` are the values, and the elements of `sub_values_list` are the sub-values in a nested dictionary format. If the input lists are of differing lengths, the function should fill in missing keys and values with `None`.
"""

def merge_lists_to_dict(keys_list, values_list, sub_values_list):
    """
    Merge three lists into a single dictionary structure.

    Args:
    keys_list (list): The list of keys for the dictionary.
    values_list (list): The list of values for the dictionary.
    sub_values_list (list): The list of sub-values for the dictionary.

    Returns:
    dict: A dictionary where the elements of `keys_list` are the keys, 
          the elements of `values_list` are the values, and the elements of `sub_values_list` are the sub-values.
    """

    # Get the maximum list length
    max_len = max(len(keys_list), len(values_list), len(sub_values_list))

    # Fill the lists with None up to maximum length
    keys_list += [None] * (max_len - len(keys_list))
    values_list += [None] * (max_len - len(values_list))
    sub_values_list += [None] * (max_len - len(sub_values_list))

    result = {}

    # Create the dictionary
    for key, value, sub_value in zip(keys_list, values_list, sub_values_list):
        if key not in result:
            result[key] = {value: sub_value}
        else:
            result[key][value] = sub_value

    return result