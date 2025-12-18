"""
QUESTION:
Create a function `format_json` that takes an unformatted JSON string as input and returns the formatted JSON string with neat indentation. The function should use the `json` standard library to parse and format the JSON string. The output should be formatted with 4-space indentation. The input string will contain nested JSON objects and arrays.
"""

import json

def format_json(unformatted_json):
    dict_obj = json.loads(unformatted_json)
    return json.dumps(dict_obj, indent=4)