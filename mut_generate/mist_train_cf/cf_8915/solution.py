"""
QUESTION:
Create a function called `process_json_data` that takes a JSON string as input and returns a dictionary. The function should convert the JSON string into a dictionary and then iterate through each key-value pair. 

For the 'name' key, the value must be a string. For the 'age' key, the value must be an integer. For the 'city' key, the value must be a string with a length greater than 10 characters. If any of these conditions are not met, the function should raise an exception with an appropriate error message. 

Any key-value pairs that do not have a key of 'name', 'age', or 'city' should be added to the returned dictionary. If the input JSON string is invalid, the function should handle the `json.JSONDecodeError` exception.
"""

import json

def process_json_data(json_string):
    try:
        data = json.loads(json_string)
        result = {}
        
        for key, value in data.items():
            if key == 'name':
                if not isinstance(value, str):
                    raise Exception("The value for key 'name' must be a string.")
            elif key == 'age':
                if not isinstance(value, int):
                    raise Exception("The value for key 'age' must be an integer.")
            elif key == 'city':
                if not isinstance(value, str):
                    raise Exception("The value for key 'city' must be a string.")
                if len(value) <= 10:
                    raise Exception("The length of the value for key 'city' must be greater than 10 characters.")
            else:
                result[key] = value

        return result

    except json.JSONDecodeError:
        raise Exception("Invalid JSON string.")
    except Exception as e:
        raise Exception(str(e))