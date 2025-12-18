"""
QUESTION:
Write a function `is_isogram` that takes a string as input and returns `True` if the string is an isogram (a word or phrase without a repeating letter) and `False` otherwise. The function should ignore spaces, punctuation marks, and be case-insensitive. It should also support multi-byte characters.
"""

def is_isogram(string):
    # Process the string to remove spaces, punctuation and make it lower case
    processed_string = ''.join(e for e in string if e.isalnum()).lower()

    # Compare the length of string with the length of set of characters. 
    # If equal, then it's isogram.
    return len(processed_string) == len(set(processed_string))