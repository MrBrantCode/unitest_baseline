"""
QUESTION:
Write a function `capitalize_string` that takes a string as input and returns the string with the first letter of each word capitalized and the rest of the letters in lowercase. The function should also handle punctuation marks by leaving them unchanged.
"""

def capitalize_string(s):
    """
    This function takes a string as input, capitalizes the first letter of each word, 
    and makes the rest of the letters lowercase. Punctuation marks are left unchanged.

    Parameters:
    s (str): The input string.

    Returns:
    str: The formatted string.
    """
    result = ''
    cap = True
    for char in s:
        if char.isalpha():
            if cap:
                result += char.upper()
                cap = False
            else:
                result += char.lower()
        else:
            result += char
            if char.isspace():
                cap = True
    return result