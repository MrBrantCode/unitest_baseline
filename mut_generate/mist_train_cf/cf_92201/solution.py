"""
QUESTION:
Implement a function `parse_json(json_data)` that takes a JSON object as input and returns a list of dictionaries, where each dictionary contains a key-value pair from the JSON object. The function should handle nested dictionaries and arrays, using a dot notation for nested keys and square brackets for array indexes.
"""

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