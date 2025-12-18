"""
QUESTION:
Write a function named `find_max_keys` that takes a dictionary `d` as input and returns a list of keys corresponding to the highest value within all nested levels. In case of ties, return all keys with the highest value. The function should be able to handle nested dictionaries. The function should return the list of keys and the maximum value.
"""

def find_max_keys(d, max_keys=None, max_val=None):
    if max_keys is None:
        max_keys = []
    if max_val is None:
        max_val = float('-inf')

    for key, val in d.items():
        if isinstance(val, dict):
            sub_max_keys, sub_max_val = find_max_keys(val, max_keys, max_val)
            if sub_max_val > max_val:
                max_val = sub_max_val
                max_keys = sub_max_keys
            elif sub_max_val == max_val:
                max_keys.extend(sub_max_keys)
        else:
            if val > max_val:
                max_val = val
                max_keys = [key]
            elif val == max_val:
                max_keys.append(key)

    return max_keys, max_val