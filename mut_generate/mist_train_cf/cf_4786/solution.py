"""
QUESTION:
Create a function named `parse_json` that takes a JSON object as input. The function should parse the JSON object and return a list of key-value dictionaries where each dictionary contains a key-value pair from the JSON object. The function should handle nested dictionaries and arrays, duplicate keys, and cyclic references. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the total number of key-value pairs in the JSON object.
"""

def parse_json(json_data):
    result = []

    def parse_object(obj, prefix=""):
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_prefix = f"{prefix}.{key}" if prefix else key
                if isinstance(value, (dict, list)):
                    parse_object(value, new_prefix)
                else:
                    result.append({"key": new_prefix, "value": value})
        elif isinstance(obj, list):
            for index, value in enumerate(obj):
                new_prefix = f"{prefix}[{index}]"
                if isinstance(value, (dict, list)):
                    parse_object(value, new_prefix)
                else:
                    result.append({"key": new_prefix, "value": value})

    parse_object(json_data)
    return result