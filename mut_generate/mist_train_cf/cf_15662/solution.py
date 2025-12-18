"""
QUESTION:
Write a function named `delete_items` that takes a dictionary as input, deletes all key-value pairs where the key starts with "item" and ends with a digit, and returns a list of the deleted key-value pairs. The function should efficiently handle large dictionaries and modify the original dictionary by removing the specified key-value pairs.
"""

def delete_items(dictionary):
    deleted_items = []
    keys_to_delete = []

    # Find keys to delete
    for key in dictionary.keys():
        if key.startswith('item') and key[-1].isdigit():
            keys_to_delete.append(key)

    # Delete keys and store deleted items
    for key in keys_to_delete:
        deleted_items.append((key, dictionary[key]))
        del dictionary[key]

    return deleted_items