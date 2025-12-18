"""
QUESTION:
Write a function `validate_json` that takes a JSON string as input and returns `True` if the JSON string is valid, and `False` otherwise. 

The function should check if the "name" value is a string and has a minimum length of 3 characters, and contains only alphabetic characters. The function should also check if the "age" value is an integer and is between 18 and 99 (inclusive).

Additionally, if the JSON string contains a nested object, the function should check if the nested object has an "address" key with a non-empty string value. If the JSON string contains a nested array, the function should check if the nested array contains a "hobbies" key with a list value that has at least one string element.

The function should handle nested objects and arrays recursively. If any validation fails, the function should return `False`. If the input string is not a valid JSON, the function should also return `False`.
"""

import json

def validate_json(json_response):
    def is_valid_name(name):
        return len(name) >= 3 and name.isalpha()

    def is_valid_age(age):
        return isinstance(age, int) and 18 <= age <= 99

    def is_valid_address(address):
        return isinstance(address, str) and len(address) > 0

    def is_valid_hobbies(hobbies):
        return isinstance(hobbies, list) and len(hobbies) > 0 and all(isinstance(hobby, str) for hobby in hobbies)

    def validate_dict(dictionary):
        for key, value in dictionary.items():
            if key == "name":
                if not is_valid_name(value):
                    return False
            elif key == "age":
                if not is_valid_age(value):
                    return False
            elif isinstance(value, dict):
                if "address" in value:
                    if not is_valid_address(value["address"]):
                        return False
                if not validate_dict(value):
                    return False
            elif isinstance(value, list):
                if any(isinstance(item, dict) for item in value):
                    for item in value:
                        if isinstance(item, dict):
                            if not validate_dict(item):
                                return False
                if any("hobbies" in item for item in value):
                    for item in value:
                        if "hobbies" in item:
                            if not is_valid_hobbies(item["hobbies"]):
                                return False
        return True

    try:
        data = json.loads(json_response)
        if isinstance(data, dict):
            return validate_dict(data)
        else:
            return False
    except json.JSONDecodeError:
        return False