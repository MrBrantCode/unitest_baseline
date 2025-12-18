"""
QUESTION:
Write a function `is_json_structure_correct(json_string)` that takes a JSON string as input and returns `True` if the JSON string has a correct structure (i.e., brackets are properly opened and closed) and `False` otherwise. The function should use Python's native JSON parsing logic to validate the structure.
"""

import json

def is_json_structure_correct(json_string):
    try:
        json_object = json.loads(json_string)
    except json.decoder.JSONDecodeError as error:
        return False
    return True