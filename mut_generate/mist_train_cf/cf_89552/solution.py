"""
QUESTION:
Write a function called `convert_to_json` that takes a nested hashmap as input, converts it to a JSON string, and returns the resulting JSON string. The time complexity should not exceed O(n), where n is the total number of elements in the hashmap. The function should handle cases where the hashmap contains circular references, ensuring that the resulting JSON string is valid and does not lead to infinite recursion. Additionally, all keys in the final JSON string should be sorted in ascending order.
"""

import json

def json_encode(obj, seen=None):
    if seen is None:
        seen = set()
    if id(obj) in seen:
        return "null"
    seen.add(id(obj))
    if isinstance(obj, dict):
        return "{" + ", ".join(f'"{k}": {json_encode(v, seen)}' for k, v in sorted(obj.items())) + "}"
    elif isinstance(obj, (list, tuple)):
        return "[" + ", ".join(json_encode(x, seen) for x in obj) + "]"
    elif isinstance(obj, str):
        return json.dumps(obj)
    elif isinstance(obj, (int, float, bool)):
        return str(obj).lower()
    elif obj is None:
        return "null"
    else:
        return "null"

def convert_to_json(hashmap):
    return json_encode(hashmap)