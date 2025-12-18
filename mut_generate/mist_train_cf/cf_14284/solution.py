"""
QUESTION:
Convert the given dictionary to a new dictionary where all keys are strings and values are either integers or lists of integers. The function should be named `convert_dict`. 

The input dictionary can have both string and integer keys, but all keys in the output dictionary should be strings. If a key in the input dictionary is an integer, convert it to a string. The corresponding values in the input dictionary can be either integers or lists of integers, and these should be preserved in the output dictionary.
"""

def convert_dict(input_dict):
    """
    Converts a dictionary to a new dictionary where all keys are strings and values are either integers or lists of integers.

    Args:
        input_dict (dict): The input dictionary to be converted.

    Returns:
        dict: A new dictionary with string keys and integer or list of integer values.
    """
    output_dict = {}
    for key, value in input_dict.items():
        if not isinstance(key, str):
            key = str(key)
        output_dict[key] = value
    return output_dict