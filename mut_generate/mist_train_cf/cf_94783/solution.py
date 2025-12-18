"""
QUESTION:
Create a function named `search_key_value_pair` that takes two parameters: `searchKey` and `object`. The function should search for a key-value pair in the `object` dictionary where the key is a string, the value is a positive integer, and the key matches the `searchKey`. The function should return the key-value pair if found, or None if not found. The time complexity of the function should be O(n), where n is the number of key-value pairs in the `object`. The function should not use built-in methods such as `filter` or `find` to search for the key-value pair.
"""

def search_key_value_pair(searchKey, object):
    result = None
    for key, value in object.items():
        if isinstance(key, str) and isinstance(value, int) and value > 0:
            if key == searchKey:
                result = (key, value)
                break
    return result