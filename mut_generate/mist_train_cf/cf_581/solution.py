"""
QUESTION:
Create a function `json_to_dict` that takes a JSON string as input. The function should parse the JSON string and return a dictionary containing only the key-value pairs where the key is "name", "age", or "city". The function should handle JSON strings with nested objects and arrays, special characters in keys, different data types, duplicate keys, and large input sizes. It should also include error handling for invalid or improperly formatted JSON strings.
"""

import json

def json_to_dict(json_string):
    try:
        data = json.loads(json_string)
        if isinstance(data, dict):
            return {key: value for key, value in data.items() if key in ["name", "age", "city"]}
        else:
            return {}
    except json.JSONDecodeError:
        return {}