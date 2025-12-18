"""
QUESTION:
Write a function named `process_data` that takes a dictionary or a list of dictionaries as input, removes any key-value pairs where the key starts with an underscore, and returns the resulting data structure. The function should handle nested dictionaries and lists, as well as inconsistent data and potential errors. The function should also be able to handle non-dictionary and non-list custom objects without raising a TypeError.
"""

def process_data(data):
    """
    This function takes a dictionary or a list of dictionaries as input, removes any key-value pairs 
    where the key starts with an underscore, and returns the resulting data structure.
    
    It handles nested dictionaries and lists, as well as inconsistent data and potential errors. 
    The function can also handle non-dictionary and non-list custom objects without raising a TypeError.

    Args:
        data (dict or list): The input dictionary or list of dictionaries.

    Returns:
        dict or list: The resulting data structure after removing key-value pairs with keys starting with an underscore.
    """
    
    if type(data) == dict:
        # Recursively process the dictionary items and filter out keys starting with an underscore
        return {k: process_data(v) for k, v in data.items() if not k.startswith("_")}
    elif type(data) == list:
        # Recursively process the list items
        return [process_data(v) for v in data]
    else:
        # If the data is not a dictionary or list, return it as is
        return data