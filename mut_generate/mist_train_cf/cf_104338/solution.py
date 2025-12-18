"""
QUESTION:
Write a Python function `double_keys(dictionary)` that takes a dictionary as input, returns a list containing all the keys in the dictionary, but with each key repeated twice, and ignores any keys that start with a vowel.
"""

def double_keys(dictionary):
    keys = [key for key in dictionary.keys() if not key[0].lower() in ['a', 'e', 'i', 'o', 'u']]
    return [key for key in keys for _ in range(2)]