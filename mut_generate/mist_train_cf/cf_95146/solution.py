"""
QUESTION:
Create a function called `validate_json` that takes a JSON string as input. The function should return `True` if the JSON object is valid and `False` otherwise. The JSON object is valid if it contains the fields "name", "age", "city", and "hobbies" with the following constraints: "name" is a string with a length between 5 and 20 characters, "age" is an integer greater than or equal to 21, "city" is one of "New York", "Los Angeles", "Chicago", or "San Francisco", and "hobbies" is a list of strings where each string has at least 3 characters.
"""

import json

def validate_json(json_string):
    try:
        data = json.loads(json_string)

        # Check "name" field
        if not isinstance(data.get('name'), str) or not (5 <= len(data['name']) <= 20):
            return False
        
        # Check "age" field
        if not isinstance(data.get('age'), int) or data['age'] < 21:
            return False
        
        # Check "city" field
        valid_cities = ["New York", "Los Angeles", "Chicago", "San Francisco"]
        if not isinstance(data.get('city'), str) or data['city'] not in valid_cities:
            return False
        
        # Check "hobbies" field
        if not isinstance(data.get('hobbies'), list):
            return False
        for hobby in data['hobbies']:
            if not isinstance(hobby, str) or len(hobby) < 3:
                return False
        
        # All validations passed
        return True

    except json.JSONDecodeError:
        return False