"""
QUESTION:
Write a function called `combine_lists` that takes two lists of strings as input, `keys` and `values`, and returns a dictionary. The dictionary's keys should be the strings in `keys` and the values should be the strings in `values`. The function should ignore any strings containing special characters, remove duplicate keys (keeping only the first occurrence), and ensure all values are in uppercase. The lengths of `keys` and `values` will always be the same.
"""

def combine_lists(keys, values):
    result = {}
    for i in range(len(keys)):
        key = ''.join(e for e in keys[i] if e.isalnum())
        if key not in result and key != "":
            result[key] = values[i].upper()
    return result