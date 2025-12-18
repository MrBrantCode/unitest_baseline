"""
QUESTION:
Write a Python function named `parse_json_data` that reads and parses JSON data. The function should take a JSON string as input and return a Python dictionary. The function should also handle cases where the input is not a valid JSON string.
"""

import json

def parse_json_data(json_string):
    """
    This function reads and parses a given JSON string into a Python dictionary.
    
    Args:
        json_string (str): A JSON string.
    
    Returns:
        dict: A Python dictionary representing the parsed JSON data.
    
    Raises:
        json.JSONDecodeError: If the input string is not a valid JSON.
    """
    try:
        # Attempt to parse the JSON string
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        # Handle the case where the input is not a valid JSON string
        print(f"Error: Invalid JSON string - {str(e)}")
        return None