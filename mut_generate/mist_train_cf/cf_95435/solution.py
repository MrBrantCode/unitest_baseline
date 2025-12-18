"""
QUESTION:
Create a function called `copy_dict_exclude` that takes a dictionary as input and returns a new dictionary that excludes any key-value pairs where the key starts with a vowel (a, e, i, o, or u) and any key-value pairs where the value is a string containing more than 10 characters.
"""

def copy_dict_exclude(dictionary):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return {k: v for k, v in dictionary.items() if k[0].lower() not in vowels and len(str(v)) <= 10}