"""
QUESTION:
Write a function named `parse_json_data` to read and parse JSON data. The function should take a string of JSON data as input and return a dictionary representation of the data. The function should also handle any potential errors that may occur during the parsing process.

The function should use the built-in `json` module to parse the JSON data. 

Note: The function should only read and parse JSON data and not store user preferences and settings.
"""

import json

def parse_json_data(json_string):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None