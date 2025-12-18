"""
QUESTION:
Write a function `add_key_value` to add a new key and its corresponding value to a given dictionary. The function should take in two parameters: the dictionary and a tuple containing the new key and value. The function should return the updated dictionary. The key and value can be any data type. The dictionary can contain any number of key-value pairs.
"""

def add_key_value(dictionary, new_item):
    dictionary[new_item[0]] = new_item[1]
    return dictionary