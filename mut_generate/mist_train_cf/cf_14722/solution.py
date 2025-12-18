"""
QUESTION:
Write a function named `find_value` that takes two parameters: a dictionary and a key. The function should return the value associated with the given key in the dictionary if the key exists, the key is a string, and the dictionary is not empty. Otherwise, it should return `None`.
"""

def find_value(dictionary, key):
    if not isinstance(dictionary, dict) or not isinstance(key, str):
        return None
    
    if key in dictionary:
        return dictionary[key]
    else:
        return None