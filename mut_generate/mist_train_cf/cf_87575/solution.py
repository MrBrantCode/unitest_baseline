"""
QUESTION:
Write a function named `remove_key` that takes a dictionary and a key as input. The function should return a new dictionary where the key-value pair corresponding to the given key is removed. If the key is not present in the dictionary, return a new dictionary that is identical to the input dictionary. The function should also handle nested dictionaries and should not use any built-in methods or functions such as `del`, `pop`, or `remove` for removing the key-value pair.
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