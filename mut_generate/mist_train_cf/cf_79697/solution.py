"""
QUESTION:
Create a function `get_names` that takes a JSON string as input and returns a list of all "name" values extracted from the JSON string and any nested JSON objects. The function should handle exceptions properly. The input JSON string can be nested and may contain multiple "name" keys. The function should return all "name" values. 

Restrictions: The input is a JSON string, not a file. The function should handle exceptions properly.
"""

import json

def get_names(json_str):
    try:
        obj = json.loads(json_str)
    except Exception as e:
        raise Exception(f"Error parsing JSON: {e}")

    def extract_names(obj):
        names = []
        if "name" in obj:
            names.append(obj["name"])

        for key in obj:
            if isinstance(obj[key], dict):
                names.extend(extract_names(obj[key]))

        return names

    return extract_names(obj)