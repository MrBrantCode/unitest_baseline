"""
QUESTION:
Create a function named `remove_special_chars` that takes a string as input and returns a string with the following modifications: 
- only alphabets (a-z, A-Z) and digits (0-9) are kept,
- any duplicate characters are removed,
- the string is in ascending order of characters, and
- the function is case-insensitive (treating uppercase and lowercase letters as the same character).
If the string is empty or contains no valid characters, the function should return an empty string.
"""

def remove_special_chars(string):
    """
    Removes special characters, duplicates, and returns the modified string in ascending order of characters.
    """
    cleaned_string = ""
    
    for char in string:
        if char.isalnum() and char.lower() not in cleaned_string:
            cleaned_string += char
    
    return ''.join(sorted(cleaned_string.lower()))