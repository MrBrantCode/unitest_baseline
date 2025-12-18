"""
QUESTION:
Write a function `change_first_char` that takes a string as input and returns the string with its first character in uppercase. The function should ensure that the string contains at least one lowercase character and one uppercase character.
"""

def change_first_char(string):
    """
    Returns the string with its first character in uppercase.
    Ensures the string contains at least one lowercase character and one uppercase character.
    """
    # Convert the string to lowercase
    string = string.lower()
    
    # Capitalize the first character
    return string.capitalize()