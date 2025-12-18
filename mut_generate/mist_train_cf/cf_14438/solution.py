"""
QUESTION:
Write a function `parse_json(json_str)` that takes a JSON string as input and attempts to parse it into a Python dictionary. The function should be able to handle nested dictionaries or lists and return the parsed dictionary if successful. If the JSON string contains invalid format or missing keys, the function should return an error message indicating the specific issue.
"""

import json

def parse_json(json_str):
    try:
        parsed_dict = json.loads(json_str)
        return parsed_dict
    except json.JSONDecodeError:
        return "Invalid JSON format"
    except KeyError:
        return "Missing key in JSON"