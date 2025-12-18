"""
QUESTION:
Create a function named `create_new_dict` that takes a dictionary as input and returns a new dictionary. The new dictionary should have the values from the original dictionary as keys and the keys from the original dictionary as values. The new dictionary should only include key-value pairs where the length of the key from the original dictionary is odd.
"""

def create_new_dict(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        if len(key) % 2 == 1:
            new_dict[value] = key
    return new_dict