"""
QUESTION:
Create a function named `flatten_dictionary` that takes a dictionary as input, flattens it into a single level dictionary where any nested dictionaries are combined with their parent keys using an underscore, removes any duplicate values, and returns the result. The function should be able to handle nested dictionaries of arbitrary depth and have a time complexity of O(n), where n is the total number of elements in the input dictionary. The function should use recursion to flatten the nested dictionaries.
"""

def entance(dictionary):
    """
    This function takes a dictionary as input, flattens it into a single level dictionary 
    where any nested dictionaries are combined with their parent keys using an underscore, 
    removes any duplicate values, and returns the result.

    Args:
        dictionary (dict): The input dictionary.

    Returns:
        dict: A flattened dictionary with no duplicate values.
    """
    flattened_dict = {}
    for key, value in dictionary.items():
        if isinstance(value, dict):
            flattened_value = entance(value)
            for sub_key, sub_value in flattened_value.items():
                if key:
                    if sub_key:
                        new_key = key + "_" + sub_key
                    else:
                        new_key = key
                else:
                    new_key = sub_key
                flattened_dict[new_key] = sub_value
        else:
            flattened_dict[key] = value
    # Remove duplicate values
    unique_values = list(set(flattened_dict.values()))
    unique_dict = {}
    for key, value in flattened_dict.items():
        if value in unique_values:
            unique_dict[key] = value
            unique_values.remove(value)
    return unique_dict