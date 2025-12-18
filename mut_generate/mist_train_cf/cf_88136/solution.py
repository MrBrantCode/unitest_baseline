"""
QUESTION:
Extract keys from a dictionary that do not start with 'a' and have string values, or have dictionary values containing keys with string values that include at least one digit.

The `extract_keys` function takes a dictionary `data` as input. It should exclude keys that start with 'a' and have non-string values. If a key's value is a dictionary, extract keys from the nested dictionary that have string values containing at least one digit. Return a list of tuples, where each tuple consists of a key and its corresponding value, sorted in descending order.
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

    result.sort(reverse=True)
    return result