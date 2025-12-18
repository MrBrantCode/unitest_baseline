"""
QUESTION:
Implement a function `customJsonGet(jsonString, path)` that takes a JSON-like string and a custom path as input and returns the value at the specified path within the JSON-like string.

The path syntax allows accessing nested elements of arrays and objects within the JSON-like string using the following rules:
- '/' separates levels of nesting.
- Square brackets access array elements by index.
- Double quotes access object properties by key.

The function should parse the JSON-like string into a Python data structure and traverse it according to the provided path, handling array indices and object keys correctly.
"""

import json

def customJsonGet(jsonString, path):
    data = json.loads(jsonString)
    keys = path.split('/')[1:]
    for key in keys:
        if key.startswith('['):
            index = int(key.strip('[]'))
            data = data[index]
        else:
            data = data.get(key.strip('"'))
    return data