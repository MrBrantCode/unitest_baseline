"""
QUESTION:
Write a function named `remove_item_keys` that takes a dictionary as input and returns a new dictionary with all key-value pairs removed where the key starts with the string "item".
"""

def remove_item_keys(dictionary):
    return {key: value for key, value in dictionary.items() if not key.startswith('item')}