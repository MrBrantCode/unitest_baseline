"""
QUESTION:
Write a function `default` that converts a given nested hashmap to a JSON string. The function should handle cases where the hashmap contains circular references and ensure the resulting JSON string is valid and does not lead to infinite recursion. The time complexity should not exceed O(n), where n is the total number of elements in the hashmap.
"""

import json

def default(obj):
    if not isinstance(obj, dict):
        return obj
    
    seen = {}
    
    for key, value in obj.items():
        if isinstance(value, dict):
            if id(value) in seen:
                obj[key] = None
            else:
                seen[id(value)] = value
                obj[key] = default(value)
    
    return obj