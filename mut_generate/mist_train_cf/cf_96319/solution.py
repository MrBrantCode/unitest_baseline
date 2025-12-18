"""
QUESTION:
Create a function called `construct_json_structure` that takes a nested Python dictionary as input. The dictionary can contain nested dictionaries and lists, with each list having a minimum length of 3. The function should construct a JSON structure from the input dictionary and ensure it has a minimum of 3 levels of nesting. The function should return the resulting JSON structure.
"""

import json

def construct_json_structure(data):
    return json.dumps(data, indent=4)