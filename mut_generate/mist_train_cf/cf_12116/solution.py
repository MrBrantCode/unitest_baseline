"""
QUESTION:
Write a function `get_character` that takes a string as input and returns the character at index 4 if the length of the string is greater than 4. The function should ignore leading and trailing whitespace characters and non-alphabetical characters.
"""

def get_character(astring):
    # Remove leading and trailing whitespace characters
    astring = astring.strip()
    
    # Remove non-alphabetical characters
    astring = ''.join(char for char in astring if char.isalpha())
    
    # Check if the length of the string is greater than 4
    if len(astring) > 4:
        return astring[4]
    else:
        return "String length is not greater than 4"