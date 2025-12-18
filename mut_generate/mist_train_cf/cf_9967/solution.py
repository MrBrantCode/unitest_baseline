"""
QUESTION:
Create a function `apply_uppercase_remove_duplicates` that takes a string as input and returns a string where all characters are in uppercase and all duplicate characters are removed.
"""

def apply_uppercase_remove_duplicates(string):
    string = string.upper()
    string = ''.join(sorted(set(string), key=string.index))
    return string