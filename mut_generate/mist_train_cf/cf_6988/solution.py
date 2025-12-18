"""
QUESTION:
Create a function named `parse_json` that takes a JSON object as input, extracts its keys and values (excluding nested objects and arrays), and returns them in a tabular format sorted in ascending order based on the keys.
"""

import json

def parse_json(json_object):
    result = []
    for key, value in sorted(json_object.items()):
        if isinstance(value, dict) or isinstance(value, list):
            result.append([key, json.dumps(value)])
        else:
            result.append([key, value])
    return result