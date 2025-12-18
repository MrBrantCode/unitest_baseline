"""
QUESTION:
Create a function called `remove_non_alphabetical_characters` that takes a string as input, removes all non-alphabetical characters, and converts all uppercase letters to lowercase. The function should return the modified string.
"""

def remove_non_alphabetical_characters(string):
    modified_string = ''
    for char in string:
        if char.isalpha():
            modified_string += char.lower()
    return modified_string