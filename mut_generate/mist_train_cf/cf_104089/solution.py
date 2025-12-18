"""
QUESTION:
Write a function named `sum_integers` that takes a JSON string as input, parses it into Python objects, and returns the sum of all integers in the JSON string, considering nested arrays and objects. The function should handle JSON strings containing a mix of integers, strings, lists, and dictionaries.
"""

import json

def sum_integers(json_string):
    def recursive_sum(data):
        if isinstance(data, int):
            return data
        elif isinstance(data, list):
            return sum(recursive_sum(item) for item in data)
        elif isinstance(data, dict):
            return sum(recursive_sum(item) for item in data.values())
        else:
            return 0

    json_data = json.loads(json_string)
    return recursive_sum(json_data)