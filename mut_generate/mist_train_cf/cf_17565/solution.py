"""
QUESTION:
Create a function `search_key_value_pair` that takes a string `searchKey` and a dictionary `object` as input, and returns a tuple containing the key-value pair if the key matches the `searchKey` and the value is a positive integer, or `None` if not found. The function should iterate over each key-value pair in the dictionary only once, resulting in a time complexity of O(n), where n is the number of key-value pairs in the dictionary.
"""

def search_key_value_pair(searchKey, object):
    for key, value in object.items():
        if isinstance(key, str) and isinstance(value, int) and value > 0:
            if key == searchKey:
                return (key, value)
    return None