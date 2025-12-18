"""
QUESTION:
Implement a function `count_characters` that takes a string as input and returns the number of uppercase letters, digits, and special characters in the string. The function should be case-sensitive and treat spaces as non-special characters.
"""

def count_characters(string):
    """
    This function counts the number of uppercase letters, digits, and special characters in a given string.
    
    Parameters:
    string (str): The input string to be processed.
    
    Returns:
    tuple: A tuple containing the count of uppercase letters, digits, and special characters.
    """
    upper_case = 0
    digits = 0
    special_characters = 0

    for character in string:
        if character.isupper():
            upper_case += 1
        elif character.isdigit():
            digits += 1
        elif not character.isalpha() and not character.isspace():
            special_characters += 1

    return upper_case, digits, special_characters