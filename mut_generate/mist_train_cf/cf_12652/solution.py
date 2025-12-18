"""
QUESTION:
Write a function `delete_empty_values_and_sort_dict` that takes a dictionary as input, removes all key-value pairs with empty or Falsey values, and returns a new dictionary with the remaining key-value pairs sorted in descending order based on their keys. The input dictionary can contain various types of values, including strings, integers, floats, and booleans.
"""

def delete_empty_values_and_sort_dict(input_dict):
    """
    Removes all key-value pairs with empty or Falsey values from a dictionary and 
    returns a new dictionary with the remaining key-value pairs sorted in descending order based on their keys.

    Args:
        input_dict (dict): The input dictionary.

    Returns:
        dict: A new dictionary with non-empty values sorted in descending order by keys.
    """
    # Remove empty values
    input_dict = {k: v for k, v in input_dict.items() if v}
    
    # Sort the remaining values in descending order based on their keys
    input_dict = dict(sorted(input_dict.items(), key=lambda x: x[0], reverse=True))
    
    return input_dict