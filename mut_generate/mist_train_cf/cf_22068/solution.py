"""
QUESTION:
Create a function `parse_json_data` that takes a JSON string as input, parses it, and prints the value of the 'name' key. Additionally, check if the 'age' key exists in the JSON data and print its value if it does. If the 'age' key does not exist, print a message stating that the key is not found. The function should also handle the case where a non-existent key is accessed, printing a message stating that the key is not found.

Note: Assume the JSON string is valid and can be parsed successfully.
"""

import json

def parse_json_data(json_string):
    """
    This function takes a JSON string as input, parses it, and prints the value of the 'name' key.
    It also checks if the 'age' key exists in the JSON data and prints its value if it does.
    If the 'age' key does not exist, it prints a message stating that the key is not found.
    
    Parameters:
    json_string (str): A valid JSON string.
    
    Returns:
    None
    """
    
    # Parse the JSON data
    try:
        json_data = json.loads(json_string)
    except json.JSONDecodeError:
        print("Invalid JSON string")
        return
    
    # Access the value of the 'name' key
    if 'name' in json_data:
        print("Name:", json_data['name'])
    else:
        print("Name not found")
        
    # Check if the 'age' key exists and print its value if it does
    if 'age' in json_data:
        print("Age:", json_data['age'])
    else:
        print("Age not found")
        
    # Attempt to access a non-existent key 'address'
    if 'address' in json_data:
        print("Address:", json_data['address'])
    else:
        print("Address not found")