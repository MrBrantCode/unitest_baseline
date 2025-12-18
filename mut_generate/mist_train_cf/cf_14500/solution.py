"""
QUESTION:
Create a function `swap_key_value_pairs(dictionary)` that takes a dictionary as input and returns a new dictionary where key-value pairs are swapped, but only for keys that are strings and values that are integers. All other key-value pairs should remain unchanged.
"""

def swap_key_value_pairs(dictionary):
    # Create a new dictionary to store the swapped key-value pairs
    swapped_dictionary = {}
    
    # Iterate through the original dictionary
    for key, value in dictionary.items():
        # Check if the key is a string and the value is an integer
        if isinstance(key, str) and isinstance(value, int):
            # Swap the key-value pair and add it to the new dictionary
            swapped_dictionary[value] = key
        else:
            # Add the original key-value pair to the new dictionary
            swapped_dictionary[key] = value
    
    return swapped_dictionary