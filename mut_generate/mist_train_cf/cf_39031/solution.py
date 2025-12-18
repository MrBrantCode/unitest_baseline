"""
QUESTION:
Implement a Python function `snake_to_camel` that takes a dictionary as input and returns a new dictionary with its keys converted from snake_case to camelCase. The function should not modify the original dictionary and should handle any number of underscores in the keys.
"""

def entrance(input_dict: dict) -> dict:
    camel_dict = {}
    for key, value in input_dict.items():
        words = key.split('_')
        camel_key = words[0] + ''.join(word.capitalize() for word in words[1:])
        camel_dict[camel_key] = value
    return camel_dict