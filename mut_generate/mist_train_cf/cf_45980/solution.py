"""
QUESTION:
Write a Python function named `json_to_array` that takes a JSON string as input and returns a list containing all scalar values from the JSON object, regardless of their nesting level. The function should handle nested JSON objects and arrays.
"""

import json

def json_to_array(json_string):
    json_object = json.loads(json_string)
    result_list = []

    def helper(nested_item):
        if type(nested_item) is dict:
            for key in nested_item:
                helper(nested_item[key])
        elif type(nested_item) is list:
            for element in nested_item:
                helper(element)
        else:
            result_list.append(nested_item)

    for key in json_object:
        helper(json_object[key])

    return result_list