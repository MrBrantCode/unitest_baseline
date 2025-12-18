"""
QUESTION:
Create a function named `is_unique_lowercase` that takes a string as an argument. The function should return True if all characters in the string are unique and lowercase alphabets only, and False otherwise. The function should be case-insensitive, i.e., it should convert the input string to lowercase before checking the conditions.
"""

def is_unique_lowercase(string):
    string = string.lower()
    return set(string) == set('abcdefghijklmnopqrstuvwxyz')