"""
QUESTION:
Create a function `validate_json` that takes a JSON string as input and returns a boolean value indicating whether the JSON string is valid. The JSON object is considered valid if it contains the fields "name", "age", "city", and "hobbies". The "name" field should be a string with a length between 5 and 20 characters, the "age" field should be an integer greater than or equal to 21, the "city" field should be one of "New York", "Los Angeles", "Chicago", or "San Francisco", and the "hobbies" field should be a list of strings, each containing at least 3 characters. If the JSON string is not a valid JSON object, the function should return False.
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