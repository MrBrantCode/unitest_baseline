"""
QUESTION:
Write a function called `get_character` that takes a string as a parameter. The function should return the character at index 4 of the string after removing leading/trailing whitespace characters and non-alphabetical characters, but only if the resulting string has a length greater than 4.
"""

def get_character(s):
    # Remove leading and trailing whitespace characters
    s = s.strip()
    
    # Remove non-alphabetical characters
    s = ''.join(char for char in s if char.isalpha())
    
    # Check if the length of the string is greater than 4
    if len(s) > 4:
        return s[4]
    else:
        return "String length is not greater than 4"