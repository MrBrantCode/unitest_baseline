"""
QUESTION:
Implement the `parse` function, which takes a string input conforming to the "BAP: " prefix followed by comma-separated key-value pairs. Each key can have an optional value enclosed in square brackets and separated by commas. If a key has a value, it is represented as key=value1,value2,...,valuen. If a key does not have a value, it is represented as just the key name. The function should return a dictionary containing the parsed key-value pairs. The dictionary values should be lists, which can be empty if a key does not have a value.
"""

import re

def parse(input_string):
    result = {}
    if input_string.startswith('BAP: '):
        input_string = input_string[5:]
        pairs = re.findall(r'(\w+)(?:=("[^"]*"|[^,]+))?(?:,|$)', input_string)
        for key, value in pairs:
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            if key in result:
                result[key].append(value)
            else:
                result[key] = [value] if value else []
    return result