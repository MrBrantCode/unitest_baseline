"""
QUESTION:
Write a function `get_keys_with_maximum_value` that takes a dictionary as input and returns a list of all keys that have the maximum value in the dictionary. If there are multiple keys with the maximum value, return all of them in the list. If the dictionary is empty, return an empty list.
"""

def get_keys_with_maximum_value(dictionary):
    if not dictionary:
        return []
    
    max_value = max(dictionary.values())
    keys_with_max_value = []
    
    for key, value in dictionary.items():
        if value == max_value:
            keys_with_max_value.append(key)
    
    return keys_with_max_value