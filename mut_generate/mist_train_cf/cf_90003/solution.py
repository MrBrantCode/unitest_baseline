"""
QUESTION:
Implement a function named `retrieve_value` that takes a dictionary and a key as input, and returns the value associated with the key. The function should only return the value if the key is present in the dictionary and the value is a string or a dictionary. If the value is a string, it should be converted to lowercase before returning. If the value is a dictionary, the function should recursively process the dictionary and convert any string values to lowercase. If the key is not present in the dictionary or the value is not a string or dictionary, the function should return an empty string.
"""

def retrieve_value(dictionary, key):
    if key in dictionary:
        value = dictionary[key]
        if isinstance(value, str):
            return value.lower()
        elif isinstance(value, dict):
            return {k: v.lower() if isinstance(v, str) else retrieve_value(v, k) for k, v in value.items()}
    return ''