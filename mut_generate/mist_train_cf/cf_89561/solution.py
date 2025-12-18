"""
QUESTION:
Write a function `json_to_dict` that takes a JSON string as input and returns its equivalent Python dictionary. The function should handle nested objects and arrays, and raise an `InvalidJSONFormatException` if the JSON string is invalid. Additionally, the function should check for circular references and raise a `CircularReferenceException` if one is detected.
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
        if id(obj) in [id(x) for x in ancestors]:
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