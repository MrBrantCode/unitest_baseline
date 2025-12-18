"""
QUESTION:
Create a function called `parse_json(json_str)` that takes a JSON string as input and returns a dictionary. The returned dictionary should only include the "name", "age", and "hobbies" fields from the JSON object, with the "name" field converted to uppercase letters. The function should also validate that the "age" field is a positive integer and that the "hobbies" field is a list of strings, removing any duplicate values before adding them to the dictionary. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the JSON object.
"""

import json

def parse_json(json_str):
    # Parse the JSON object
    data = json.loads(json_str)
    
    # Initialize the parsed dictionary
    parsed_dict = {}

    # Check if "name" field exists and convert it to uppercase
    if 'name' in data:
        parsed_dict['name'] = data['name'].upper()
    
    # Check if "age" field exists and is a positive integer
    if 'age' in data and isinstance(data['age'], int) and data['age'] > 0:
        parsed_dict['age'] = data['age']
    
    # Check if "hobbies" field exists and is a list of strings
    if 'hobbies' in data and isinstance(data['hobbies'], list):
        # Remove duplicate values from "hobbies" field
        hobbies = list(set(data['hobbies']))
        # Check if all values in "hobbies" field are strings
        if all(isinstance(hobby, str) for hobby in hobbies):
            parsed_dict['hobbies'] = hobbies
    
    return parsed_dict