"""
QUESTION:
Implement a function `search_key_value_pair` that searches for a specific key-value pair in a nested object. The function should take two parameters: `search_key` (a string) and `obj` (a nested object). The function should return the key-value pair if the key is a string and the value is a dictionary with at least one key-value pair where the key is a string and the value is a positive integer. If no such key-value pair is found, the function should return None.

The function must have a time complexity of O(n), where n is the number of key-value pairs in the object, and must not use built-in methods such as `filter` or `find`.
"""

def search_key_value_pair(search_key, obj):
    def search_in_obj(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(key, str) and isinstance(value, dict):
                    for k, v in value.items():
                        if isinstance(k, str) and isinstance(v, int) and v > 0:
                            if key == search_key:
                                return {key: value}
                else:
                    result = search_in_obj(value)
                    if result is not None:
                        return result
        return None

    return search_in_obj(obj)