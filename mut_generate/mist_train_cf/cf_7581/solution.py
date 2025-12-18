"""
QUESTION:
Implement a function called `retrieve_value` that takes two parameters: a dictionary and a key. The function should retrieve the value of the given key from the dictionary, handling nested dictionaries, and return it only if the key is present and the value is a string. If the value is a string, it should be converted to lowercase before returning. If the key is not present or the value is not a string, the function should return an empty string.
"""

def retrieve_value(dictionary, key):
    if key in dictionary:
        value = dictionary[key]
        if isinstance(value, str):
            return value.lower()
        elif isinstance(value, dict):
            return retrieve_value(value, key)
    return ''