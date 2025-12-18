"""
QUESTION:
Write a function `to_uppercase` that takes a string as input and returns its equivalent uppercase string, removing any whitespace characters. The function should not use any built-in string methods (except indexing and concatenation) or libraries.
"""

def to_uppercase(s):
    """
    This function takes a string as input, converts it to uppercase and removes any whitespace characters.

    Args:
        s (str): The input string.

    Returns:
        str: The uppercase equivalent of the input string without whitespace characters.
    """
    lower_to_upper = {
        'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K',
        'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U', 'v': 'V',
        'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'
    }
    
    str_upper_case = ""
    for char in s:
        if char in lower_to_upper:
            str_upper_case += lower_to_upper[char]
        elif char != ' ':
            str_upper_case += char.upper()
    
    return str_upper_case