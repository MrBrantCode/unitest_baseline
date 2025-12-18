"""
QUESTION:
Write a function called `parse_json` that takes a JSON object as input and returns a list of key-value dictionaries. The function should handle nested dictionaries and arrays, and include all key-value pairs in the result. The keys in the output dictionaries should be prefixed with their parent keys using dot notation for nested dictionaries and square brackets for array indexes.
"""

import json

def parse_json(json_data):
    result = []
    
    def parse_object(obj, prefix=""):
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_prefix = f"{prefix}.{key}" if prefix else key
                parse_object(value, new_prefix)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                new_prefix = f"{prefix}[{index}]"
                parse_object(item, new_prefix)
        else:
            result.append({"key": prefix, "value": obj})
    
    parse_object(json_data)
    return result