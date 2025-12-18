"""
QUESTION:
Write a function `extract_keys` that takes a dictionary as input. The function should extract keys that do not start with the letter 'a' and have a string value. If a nested dictionary is encountered, it should extract keys that have a value containing at least one digit. The function should return a list of tuples containing the extracted keys and their corresponding values, sorted in descending order by key.
"""

def extract_keys(dictionary):
    extracted_keys = []

    for key, value in dictionary.items():
        if key[0] != 'a' and isinstance(value, str):
            extracted_keys.append((key, value))
        elif isinstance(value, dict):
            nested_keys = extract_keys(value)
            for k, v in nested_keys:
                if any(char.isdigit() for char in v):
                    extracted_keys.append((k, v))

    extracted_keys.sort(reverse=True)

    return extracted_keys