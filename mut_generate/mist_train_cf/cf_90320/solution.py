"""
QUESTION:
Write a function called `remove_special_characters` that takes a string as input, removes all special characters except for the '@' symbol, converts all uppercase letters to lowercase, removes any duplicate characters, and sorts the resulting string in alphabetical order. The function should return the modified string.
"""

def remove_special_characters(string):
    # Remove special characters and convert to lowercase
    modified_string = ''.join([char.lower() for char in string if char.isalnum() or char == '@'])
    
    # Sort and remove duplicates
    modified_string = ''.join(sorted(set(modified_string)))
    
    return modified_string