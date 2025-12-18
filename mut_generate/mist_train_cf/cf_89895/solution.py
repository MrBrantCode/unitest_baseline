"""
QUESTION:
Write a function named `get_third_nested_element` that takes a deeply nested JSON object as input. The function should return the data of the third element in a deeply nested JSON array within the JSON object. The function should have a time complexity of O(N), where N is the total number of elements in the JSON object, and minimize memory usage by only storing one element in memory at a time.
"""

import json

def get_third_nested_element(json_obj):
    def traverse(obj):
        if isinstance(obj, list):
            for item in obj:
                yield from traverse(item)
        elif isinstance(obj, dict):
            for key, value in obj.items():
                yield from traverse(value)
        else:
            yield obj
    
    count = 0
    for element in traverse(json_obj):
        if count == 2:
            return element
        count += 1
    return None