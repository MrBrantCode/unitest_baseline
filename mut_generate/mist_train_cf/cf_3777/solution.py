"""
QUESTION:
Create a function `extract_keys` that takes a dictionary `data` as input. The function should return a list of tuples, where each tuple consists of a key and its corresponding value. The function should ignore any keys that start with the letter 'a' and have a value that is not a string. If a nested dictionary is encountered as a value, only extract the keys from the nested dictionary that have values containing at least one digit. The extracted keys should be sorted in descending order.
"""

def extract_keys(data):
    result = []

    for key, value in data.items():
        if key[0] != 'a' and (type(value) == str or isinstance(value, dict)):
            if type(value) == str:
                result.append((key, value))
            elif isinstance(value, dict):
                nested_keys = [k for k, v in value.items() if any(c.isdigit() for c in str(v))]
                result.append((key, {k: value[k] for k in nested_keys}))

    result.sort(key=lambda x: x[0], reverse=True)
    return result