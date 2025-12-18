"""
QUESTION:
Create a function called `filter_names` that takes a list of names as input, filters out names that do not contain any vowels (ignoring case sensitivity), removes duplicates, and returns the remaining names in alphabetical order.
"""

def filter_names(names):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_names = [name for name in names if any(vowel in name.lower() for vowel in vowels)]
    return sorted(set(filtered_names))