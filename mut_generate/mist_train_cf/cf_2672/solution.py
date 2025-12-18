"""
QUESTION:
Create a function `remove_key` that takes a dictionary and a key as input, and returns a new dictionary with the key-value pair removed. The function should handle cases where the key is not present in the dictionary, and also handle nested dictionaries. The function should not modify the original dictionary and should not use built-in methods such as `del`, `pop`, or `remove`.
"""

def remove_key(dictionary, key):
    new_dict = {}
    for k, v in dictionary.items():
        if k == key:
            continue
        if isinstance(v, dict):
            new_dict[k] = remove_key(v, key)
        else:
            new_dict[k] = v
    return new_dict