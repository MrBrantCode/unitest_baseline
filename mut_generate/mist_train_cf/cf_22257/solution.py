"""
QUESTION:
Create a function named `to_dict` that takes two lists of equal length as input and returns a dictionary where the elements of the first list are the keys and the elements of the second list are the corresponding values. The function should keep the last value encountered for duplicate keys and return an empty dictionary if the input lists are empty. Additionally, it should only include keys with a length of at least 3 characters in the resulting dictionary.
"""

def to_dict(keys, values):
    return {key: value for key, value in zip(keys, values) if len(key) >= 3}