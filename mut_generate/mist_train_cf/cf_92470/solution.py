"""
QUESTION:
Add a list to a specific key at a depth of at least 3 levels in a nested JSON document.

Implement a function named `add_list_to_nested_json` that takes in two parameters: `json_data` (a string representing the nested JSON document) and `key_path` (a list of strings representing the key path to the target key). The function should parse the JSON document into a Python dictionary, traverse to the target key, add the list `[1, 2, 3]` to the key, and return the updated JSON document as a string.

Restrictions: The key should be located at a depth of at least 3 levels from the root of the JSON structure.
"""

import json

def add_list_to_nested_json(json_data, key_path):
    """
    This function adds a list to a specific key at a depth of at least 3 levels in a nested JSON document.

    Args:
    json_data (str): A string representing the nested JSON document.
    key_path (list): A list of strings representing the key path to the target key.

    Returns:
    str: The updated JSON document as a string.
    """
    # Parse JSON into dictionary
    data = json.loads(json_data)

    # Traverse to the desired key
    current_data = data
    for key in key_path[:-1]:
        current_data = current_data[key]

    # Add list to the key
    current_data[key_path[-1]].extend([1, 2, 3])

    # Convert back to JSON
    updated_json = json.dumps(data)

    return updated_json