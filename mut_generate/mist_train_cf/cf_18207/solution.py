"""
QUESTION:
Write a function called `delete_item` that deletes a specific item with the given key from a dictionary, including nested dictionaries, recursively. The function should have a time complexity of O(n) and a space complexity of O(1). The function should take two parameters: the dictionary and the key of the item to delete.
"""

def delete_item(dictionary, key):
    for k, v in dictionary.items():
        if k == key:
            del dictionary[k]
            return
        elif isinstance(v, dict):
            delete_item(v, key)