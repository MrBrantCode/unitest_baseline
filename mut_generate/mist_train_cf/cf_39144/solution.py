"""
QUESTION:
Implement a function `check_missing_key(pd_keys, key)` that checks if a key is missing from a dictionary based on specific conditions. The function should take a dictionary `pd_keys` and a string `key` as parameters and return `True` if the `key` is missing from the dictionary under the following conditions:
- The `key` is not present in the `pd_keys` dictionary.
- The `key` ends with '.weight' and the substring obtained by removing the '.weight' suffix is not present in the `pd_keys` dictionary.
- The `key` ends with '.bias' and the substring obtained by removing the '.bias' suffix is not present in the `pd_keys` dictionary.
Otherwise, the function should return `False`.
"""

def check_missing_key(pd_keys, key):
    if key not in pd_keys:
        return True
    if key.endswith('.weight') and key[:-7] not in pd_keys:
        return True
    if key.endswith('.bias') and key[:-5] not in pd_keys:
        return True
    return False