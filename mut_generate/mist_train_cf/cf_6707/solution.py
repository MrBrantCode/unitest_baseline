"""
QUESTION:
Write a function called `json_to_dict` that converts a given JSON string into its Python dictionary equivalent. The function should handle JSON strings with nested objects and arrays. It should also detect and raise exceptions for invalid JSON strings and circular references.
"""

import json

class CircularReferenceException(Exception):
    pass

class InvalidJSONFormatException(Exception):
    pass

def json_to_dict(json_string):
    try:
        data = json.loads(json_string)
    except json.JSONDecodeError:
        raise InvalidJSONFormatException("Missing closing bracket in the JSON string.")

    def check_circular_reference(obj, ancestors):
        if id(obj) in [id(ancestor) for ancestor in ancestors]:
            raise CircularReferenceException("Circular reference detected in the JSON string.")
        if isinstance(obj, dict):
            ancestors.append(obj)
            for value in obj.values():
                check_circular_reference(value, ancestors)
            ancestors.pop()
        elif isinstance(obj, list):
            for item in obj:
                check_circular_reference(item, ancestors)
        elif not isinstance(obj, (str, int, float, bool)):
            raise InvalidJSONFormatException("Invalid value in the JSON string.")

    check_circular_reference(data, [])

    return data