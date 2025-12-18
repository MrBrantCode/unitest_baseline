"""
QUESTION:
Write a function `extract_value` that takes two parameters: `input_string` and `key`, both of type `str`. The `input_string` is a series of key-value pairs separated by a comma and a space. Each key-value pair is separated by an equals sign, and values can be enclosed in single quotes. The function should return the value associated with the given `key` as a string. If the `key` is not found, return "Key not found".
"""

def extract_value(input_string: str, key: str) -> str:
    pairs = input_string.split(', ')
    for pair in pairs:
        k, v = pair.split('=')
        if k.strip() == key:
            return v.strip().strip("'")
    return "Key not found"