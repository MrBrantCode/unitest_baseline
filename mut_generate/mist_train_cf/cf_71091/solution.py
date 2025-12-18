"""
QUESTION:
Write a function named `sort_dict_list` that sorts a list of dictionaries in ascending order according to a specific key. The function should be able to handle nested dictionaries. The list of dictionaries may contain different keys and not all dictionaries may have the same keys.
"""

def sort_dict_list(dict_list, key):
    """
    Sorts a list of dictionaries in ascending order according to a specific key.
    
    Parameters:
    dict_list (list): A list of dictionaries to be sorted.
    key (str): The key according to which the list will be sorted.
    
    Returns:
    list: The sorted list of dictionaries.
    """
    
    # Define a function to get the value of a key from a nested dictionary
    def get_value(dictionary, key):
        # Split the key by '.' to handle nested dictionaries
        key_parts = key.split('.')
        
        # Initialize the current dictionary
        current_dict = dictionary
        
        # Iterate over the key parts
        for part in key_parts:
            # If the part is not in the current dictionary, return None
            if part not in current_dict:
                return None
            # Otherwise, update the current dictionary
            current_dict = current_dict[part]
        
        # Return the value of the key
        return current_dict
    
    # Sort the list of dictionaries using the custom get_value function
    return sorted(dict_list, key=lambda x: get_value(x, key))