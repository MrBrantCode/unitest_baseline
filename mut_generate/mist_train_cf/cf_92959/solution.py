"""
QUESTION:
Create a function called `add_to_dictionary` that adds a key-value pair to a dictionary. The key must be a string that is alphanumeric and between 1 and 10 characters in length. The value must be a positive integer. The dictionary can only hold a maximum of 100 key-value pairs. If the key-value pair meets these conditions, it should be added to the dictionary; otherwise, an error message should be returned.
"""

def add_to_dictionary(dictionary, key, value):
    if len(key) <= 10 and key.isalnum() and value > 0 and len(dictionary) < 100:
        dictionary[key] = value
        return "Key-value pair added successfully."
    else:
        return "Invalid key-value pair."