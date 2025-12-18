"""
QUESTION:
Write a function called `valid_number` that takes a string as input and returns True if the string contains a valid number, False otherwise. A valid number is defined as a sequence of at least 3 characters that starts with a letter and ends with a digit, and consists only of digits and alphabetic characters.
"""

def valid_number(s):
    """
    Checks if a string contains a valid number.

    A valid number is defined as a sequence of at least 3 characters 
    that starts with a letter and ends with a digit, and consists only 
    of digits and alphabetic characters.

    Parameters:
    s (str): The input string.

    Returns:
    bool: True if the string contains a valid number, False otherwise.
    """
    if len(s) < 3:
        return False
    if not s[0].isalpha():
        return False
    if not s[-1].isdigit():
        return False
    for char in s:
        if not char.isalnum():
            return False
    return True