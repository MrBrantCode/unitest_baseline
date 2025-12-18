"""
QUESTION:
Write a function `search_key_value_pair(searchKey, object)` that takes two parameters: `searchKey` (a string to be searched in the dictionary) and `object` (a dictionary). The function should return the key-value pair from the dictionary if the key matches the `searchKey` and the value is a positive integer. If no such pair is found, the function should return `None`. The search should only consider key-value pairs where the key is a string.
"""

def search_key_value_pair(searchKey, object):
    result = None
    
    for key, value in object.items():
        if isinstance(key, str) and isinstance(value, int) and value > 0:
            if key == searchKey:
                result = (key, value)
                break
    
    if result is None:
        return None
    else:
        return result