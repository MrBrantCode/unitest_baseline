"""
QUESTION:
Create a function called `remove_special_characters` that takes a string as input and returns the modified string after removing all special characters except '@', converting to lowercase, sorting in alphabetical order, and removing duplicates. The special characters include any character that is not a letter, number, or the '@' symbol.
"""

def remove_special_characters(string):
    # Remove special characters and convert to lowercase
    modified_string = ''.join([char.lower() for char in string if char.isalnum() or char == '@'])
    
    # Sort and remove duplicates
    modified_string = ''.join(sorted(set(modified_string)))
    
    return modified_string