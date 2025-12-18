"""
QUESTION:
Remove special characters from a sentence.

Implement a function `remove_special_characters` that takes a string as input and returns the string with all special characters removed. Special characters are defined as any characters that are not alphanumeric or spaces.

Restrictions: The function should only remove special characters and not modify any other characters in the string.
"""

def remove_special_characters(s):
    return ''.join(char for char in s if char.isalnum() or char.isspace())