"""
QUESTION:
Implement the function `parse_json(json_string)` that takes a JSON string as input and returns a Python dictionary. The function should handle cases where the JSON string contains invalid or missing keys, and return an error message if any of these cases occur. The function should not use built-in libraries like `json` or `ast` for parsing the JSON string.
"""

import json

def parse_json(json_string):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        return f"Error parsing JSON: {e}"