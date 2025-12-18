"""
QUESTION:
Create a function named `parse_json` that takes a JSON string as input and returns a dictionary containing only the "name", "age", and "hobbies" fields. The "name" field should be converted to uppercase letters. The function should validate that the "age" field is a positive integer and the "hobbies" field is a list of strings with no duplicates. The function should achieve a time complexity of O(n) and a space complexity of O(1).
"""

import json

def parse_json(json_str):
    data = json.loads(json_str)
    parsed_dict = {}

    if 'name' in data:
        parsed_dict['name'] = data['name'].upper()
    
    if 'age' in data and isinstance(data['age'], int) and data['age'] > 0:
        parsed_dict['age'] = data['age']
    
    if 'hobbies' in data and isinstance(data['hobbies'], list):
        hobbies = list(set(data['hobbies']))
        if all(isinstance(hobby, str) for hobby in hobbies):
            parsed_dict['hobbies'] = hobbies
    
    return parsed_dict