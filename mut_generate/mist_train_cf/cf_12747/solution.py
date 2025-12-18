"""
QUESTION:
Add the given list to a specific key at a depth of at least 3 levels in a nested JSON document using Python. Function should be able to parse a given JSON string into a dictionary, traverse the dictionary structure to reach the desired key, and assign the list to that key.
"""

import json

def add_to_key(json_data, key_path, value):
    """
    Adds a list to a specific key at a depth of at least 3 levels in a nested JSON document.

    Args:
    json_data (str): The JSON document as a string.
    key_path (list): A list of keys representing the path to the target key.
    value (list): The list to be added to the target key.

    Returns:
    str: The updated JSON document as a string.
    """
    # Parse JSON into dictionary
    data = json.loads(json_data)
    
    # Traverse to the desired key
    target_key = data
    for key in key_path[:-1]:
        target_key = target_key[key]
    
    # Add list to the key
    target_key[key_path[-1]].extend(value)
    
    # Convert back to JSON
    updated_json = json.dumps(data)
    
    return updated_json