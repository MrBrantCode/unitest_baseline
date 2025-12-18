"""
QUESTION:
Write a function named 'extract_key' that takes a dictionary and a key as input, where the dictionary contains string keys and integer values. The function should return the corresponding value if the key exists in the dictionary, and None otherwise. The function must be able to handle dictionaries with up to 1000 key-value pairs.
"""

def extract_key(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        return None