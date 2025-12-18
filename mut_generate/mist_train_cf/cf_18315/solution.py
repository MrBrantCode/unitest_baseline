"""
QUESTION:
Create a function `json_to_dict` that takes in a JSON string as input and returns a valid Python dictionary. The input JSON string can contain nested objects and arrays with multiple levels of nesting. If the JSON string contains duplicate keys, the function should overwrite the existing value with the new value. The function should handle invalid JSON strings by catching any exceptions raised during parsing and printing an error message.
"""

import json

def json_to_dict(json_str):
    result = {}

    def parse_dict(data, obj):
        for key, value in data.items():
            if isinstance(value, dict):
                obj[key] = {}
                parse_dict(value, obj[key])
            elif isinstance(value, list):
                obj[key] = []
                parse_list(value, obj[key])
            else:
                obj[key] = value

    def parse_list(data, arr):
        for item in data:
            if isinstance(item, dict):
                obj = {}
                arr.append(obj)
                parse_dict(item, obj)
            elif isinstance(item, list):
                sub_arr = []
                arr.append(sub_arr)
                parse_list(item, sub_arr)
            else:
                arr.append(item)

    try:
        parsed_data = json.loads(json_str)
        if isinstance(parsed_data, dict):
            parse_dict(parsed_data, result)
        elif isinstance(parsed_data, list):
            result = []
            parse_list(parsed_data, result)
    except json.JSONDecodeError:
        print("Invalid JSON string.")

    return result