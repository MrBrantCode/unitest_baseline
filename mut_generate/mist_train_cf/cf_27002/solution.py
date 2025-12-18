"""
QUESTION:
Implement a function `deep_camel_case_transform` that takes a dictionary as input and returns a new dictionary with all keys and nested keys converted from snake_case to camelCase. The function should handle dictionaries nested within other dictionaries and lists of dictionaries.
"""

def deep_camel_case_transform(data):
    if isinstance(data, dict):
        camelized_data = {}
        for key, value in data.items():
            camel_key = ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(key.split('_')))
            camelized_data[camel_key] = deep_camel_case_transform(value)
        return camelized_data
    elif isinstance(data, list):
        return [deep_camel_case_transform(item) for item in data]
    else:
        return data