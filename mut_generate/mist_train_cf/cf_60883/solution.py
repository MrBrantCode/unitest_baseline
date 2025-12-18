"""
QUESTION:
Design a function called `ascii_checker` that takes a string as input and returns `True` if the string is composed entirely of ASCII printable characters (space to tilde, ASCII values 32 to 126) and `False` otherwise.
"""

def ascii_checker(input_string):
    """
    Checks if the input string is composed entirely of ASCII printable characters.
    
    Args:
        input_string (str): The input string to be checked.

    Returns:
        bool: True if the string is composed entirely of ASCII printable characters, False otherwise.
    """
    for character in input_string:
        if ord(character) < 32 or ord(character) > 126:
            return False
    return True