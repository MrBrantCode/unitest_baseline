"""
QUESTION:
Write a function called `generate_dict` that takes a string in the format "KEY1:VALUE1,KEY2:VALUE2,KEY3:VALUE3" as input and returns a dictionary. The function should split the input string into key-value pairs, remove leading/trailing spaces, and store the pairs in a dictionary. If the input string is empty or contains only spaces, or if a key or value is empty after removing leading/trailing spaces, return an empty dictionary or skip that key-value pair respectively.
"""

def generate_dict(text):
    if not text.strip():
        return {}

    pairs = text.split(',')

    result = {}

    for pair in pairs:
        key, value = pair.split(':')
        key = key.strip()
        value = value.strip()

        if key and value:
            result[key] = value

    return result