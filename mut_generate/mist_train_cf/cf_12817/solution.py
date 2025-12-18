"""
QUESTION:
Create a function named `is_unique_lowercase` that takes a string as input and returns a boolean indicating whether all characters in the string are unique and lowercase alphabets only. The function should ignore case sensitivity by converting the input string to lowercase before checking.
"""

def is_unique_lowercase(string):
    # Convert the string to lowercase
    string = string.lower()
    
    # Check if all characters are unique lowercase alphabets only
    unique_chars = set(string)
    lowercase_alphabets = set('abcdefghijklmnopqrstuvwxyz')
    
    return unique_chars == lowercase_alphabets