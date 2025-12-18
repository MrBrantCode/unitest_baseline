"""
QUESTION:
Write a function named `delete_item` that takes a dictionary and a key as parameters, and deletes the key-value pair with the given key from the dictionary recursively if it exists, maintaining a time complexity of O(n) and a space complexity of O(1).
"""

def delete_item(dictionary, key):
    for k, v in dictionary.items():
        if k == key:
            del dictionary[k]
            return
        elif isinstance(v, dict):
            delete_item(v, key)