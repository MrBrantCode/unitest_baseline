"""
QUESTION:
Construct a function `filter_names` that takes a list of names as input and returns a new list containing only the names that have a length greater than 4 and contain at least one vowel. The function should be case-insensitive when checking for vowels.
"""

def filter_names(names):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [name for name in names if len(name) > 4 and any(vowel in name.lower() for vowel in vowels)]