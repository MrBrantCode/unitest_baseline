"""
QUESTION:
Create a function `unique_dict` that takes a dictionary as input and returns a new dictionary where all keys and values are unique. If a duplicate value is found, exclude it from the new dictionary.
"""

def unique_dict(input_dict):
    """
    This function takes a dictionary as input and returns a new dictionary 
    where all keys and values are unique. If a duplicate value is found, 
    exclude it from the new dictionary.

    Args:
        input_dict (dict): The input dictionary.

    Returns:
        dict: A new dictionary with unique keys and values.
    """
    new_dict = {}
    for key, value in input_dict.items():
        if value not in new_dict.values() and key not in new_dict:
            new_dict[key] = value
    return new_dict