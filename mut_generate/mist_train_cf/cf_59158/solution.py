"""
QUESTION:
Write a function `is_isogram(string)` that takes a string as input and returns `True` if the string is an isogram (a word or phrase without a repeating letter) and `False` otherwise. The function should be case-insensitive, ignore white spaces, and consider only alphabetic characters (ignoring punctuation, numerical characters, and special characters).
"""

def is_isogram(string):
    string = string.replace(" ","").lower()
    string = ''.join(e for e in string if e.isalpha())
    return len(string) == len(set(string))