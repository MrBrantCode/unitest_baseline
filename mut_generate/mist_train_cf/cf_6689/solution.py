"""
QUESTION:
Write a function named `convert_to_json` that takes a nested hashmap as input and returns a JSON string representation of the hashmap. The function should handle circular references and sort the keys in the JSON string in ascending order. The time complexity of the function should not exceed O(n), where n is the total number of elements in the hashmap.
"""

import json

def convert_to_json(hashmap):
    seen = set()
    def json_encode(obj):
        if id(obj) in seen:
            return "null"
        seen.add(id(obj))
        if isinstance(obj, dict):
            return "{" + ", ".join(f'"{k}": {json_encode(v)}' for k, v in sorted(obj.items())) + "}"
        elif isinstance(obj, (list, tuple)):
            return "[" + ", ".join(json_encode(x) for x in obj) + "]"
        elif isinstance(obj, str):
            return json.dumps(obj)
        elif isinstance(obj, (int, float, bool)):
            return str(obj).lower()
        elif obj is None:
            return "null"
        else:
            return "null"
    return json_encode(hashmap)