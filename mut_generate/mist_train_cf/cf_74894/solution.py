"""
QUESTION:
Create a function `is_isogram(string)` that determines whether a given string is an isogram, a word or phrase without a repeating letter, regardless of case. The function should treat a blank string as an isogram and consider non-alphabet characters as part of the string. The function should return `True` if the string is an isogram and `False` otherwise.
"""

def is_isogram(string):
    string = ''.join(e for e in string if e.isalpha())  # Remove non-alphabet characters
    string = string.lower()  # Convert to lowercase
    return len(string) == len(set(string))  # Compare lengths of original string and unique characters