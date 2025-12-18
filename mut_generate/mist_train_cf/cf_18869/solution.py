"""
QUESTION:
Create a function called `flatten_dict` that takes a dictionary as input and returns a flattened list of its values. The input dictionary can contain multiple levels of nesting. The function should handle this nesting recursively and return a list of all values in the dictionary. The order of values in the output list is not specified.
"""

def flatten_dict(dictionary):
    """
    This function takes a dictionary as input and returns a flattened list of its values.
    
    The input dictionary can contain multiple levels of nesting. The function handles this nesting recursively 
    and returns a list of all values in the dictionary.
    
    :param dictionary: The input dictionary
    :return: A list of values from the dictionary
    """
    flattened_list = []
    for value in dictionary.values():
        if isinstance(value, dict):
            flattened_list.extend(flatten_dict(value))
        else:
            flattened_list.append(value)
    return flattened_list