"""
QUESTION:
Create a function called `count_values` that takes a JSON structure as a string input and returns the total count of all the values in the structure, including those in nested objects and arrays, and regardless of their data type. The input JSON structure can contain any valid JSON data, including objects, arrays, strings, numbers, booleans, and null values.
"""

import json

def count_values(json_structure):
    count = 0
    
    def count_recursive(obj):
        nonlocal count
        if isinstance(obj, dict):
            for value in obj.values():
                count_recursive(value)
        elif isinstance(obj, list):
            for item in obj:
                count_recursive(item)
        else:
            count += 1
    
    json_data = json.loads(json_structure)
    count_recursive(json_data)
    return count