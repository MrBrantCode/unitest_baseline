"""
QUESTION:
Write a function `delete_items(dictionary)` that takes a dictionary as input, deletes all key-value pairs whose key starts with "item" and ends with a digit, and returns a list of the deleted key-value pairs. The function should modify the original dictionary and handle large dictionaries efficiently without causing memory or performance issues.
"""

def delete_items(dictionary):
    deleted_items = [key_value for key_value in list(dictionary.items()) if key_value[0].startswith('item') and key_value[0][-1].isdigit()]
    for key, _ in deleted_items:
        del dictionary[key]
    return deleted_items