"""
QUESTION:
Create a function called `update_nested_dict` that takes in a dictionary and a list of keys as input. The function should return the value associated with the last key in the list, and also update this value to a new value provided as input. If any key in the list does not exist in the dictionary, the function should handle the error and return an error message.
"""

def update_nested_dict(nested_dict, keys, new_value):
    """
    This function updates the value of a key in a nested dictionary and returns the updated value.
    
    Parameters:
    nested_dict (dict): The dictionary to be updated.
    keys (list): A list of keys representing the path to the value in the nested dictionary.
    new_value: The new value to be assigned to the key.
    
    Returns:
    The updated value if successful, otherwise an error message.
    """
    
    # Make a copy of the original dictionary to avoid modifying it directly
    temp_dict = nested_dict.copy()
    
    # Initialize a variable to store the current dictionary
    current_dict = temp_dict
    
    # Traverse through the keys
    for i, key in enumerate(keys):
        # If this is not the last key, update the current dictionary
        if i < len(keys) - 1:
            # Check if the key exists in the current dictionary
            if key in current_dict:
                current_dict = current_dict[key]
            else:
                return f"Error: Key '{key}' not found in the dictionary."
        # If this is the last key, update its value
        else:
            # Check if the key exists in the current dictionary
            if key in current_dict:
                old_value = current_dict[key]
                current_dict[key] = new_value
                return new_value
            else:
                return f"Error: Key '{key}' not found in the dictionary."