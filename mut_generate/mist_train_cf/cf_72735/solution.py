"""
QUESTION:
Construct a function named `remove_key` that takes two parameters, a dictionary `d` and a key `key`, to safely and efficiently erase a key-value pair from the dictionary. The function should handle edge cases where the key does not exist in the dictionary and also remove the key-value pair from any nested dictionaries. The function should modify the original dictionary and return it.
"""

def remove_key(d, key):
    """ This function safely removes a key-value pair from the dictionary as well as from any nested dictionaries """
    if key in d:
        del d[key]
    for v in d.values():
        if isinstance(v, dict): 
            remove_key(v, key)
    return d