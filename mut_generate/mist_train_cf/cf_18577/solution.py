"""
QUESTION:
Create a function named `extract_keys` that takes a dictionary as input. The function should extract keys that do not start with 'a' and have string values. If a nested dictionary is encountered, it should extract keys with values containing at least one digit. The function should return a list of tuples, each containing a key and its value, sorted in descending order of keys.
"""

def extract_keys(dictionary):
    extracted_keys = []
    for key, value in dictionary.items():
        if key[0] != 'a' and isinstance(value, str):
            if any(char.isdigit() for char in value):
                extracted_keys.append((key, value))
        elif isinstance(value, dict):
            nested_keys = extract_keys(value)
            extracted_keys.extend([(key + '.' + k, v) for k, v in nested_keys if any(char.isdigit() for char in str(v))])
    extracted_keys.sort(reverse=True)
    return extracted_keys