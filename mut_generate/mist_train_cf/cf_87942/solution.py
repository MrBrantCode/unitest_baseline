"""
QUESTION:
Implement a function `recursive_delete(dictionary, key)` that deletes a specific item from a nested dictionary. The function should recursively search for the key in the dictionary and its nested dictionaries, and remove the key-value pair if found. The function should maintain a time complexity of O(n) and a space complexity of O(1), and should not use any built-in Python functions or methods to delete the item.
"""

def recursive_delete(dictionary, key):
    deleted = False
    for k in list(dictionary.keys()):
        if isinstance(dictionary[k], dict):
            deleted = recursive_delete(dictionary[k], key) or deleted
        elif k == key:
            deleted = True
            dictionary.pop(k)
    return deleted