"""
QUESTION:
Write a function `calculate_sum` that takes a JSON string as input, parses it into Python objects, and returns the sum of all integers in the JSON string that are not divisible by 5. The function should handle nested arrays and objects in the JSON string.
"""

import json

def calculate_sum(json_string):
    data = json.loads(json_string)
    total_sum = 0
    for value in iterate_values(data):
        if isinstance(value, int) and value % 5 != 0:
            total_sum += value
    return total_sum

def iterate_values(data):
    if isinstance(data, dict):
        for value in data.values():
            yield from iterate_values(value)
    elif isinstance(data, list):
        for value in data:
            yield from iterate_values(value)
    else:
        yield data