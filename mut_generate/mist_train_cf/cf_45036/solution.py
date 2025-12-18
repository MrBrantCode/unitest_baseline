"""
QUESTION:
Create a function named `alphanumeric_sequences` that takes an alphanumeric string `s` as input and returns two separate strings: one containing all the alphabetic characters and the other containing all the numeric characters.
"""

def alphanumeric_sequences(s):
    """
    This function separates an alphanumeric string into two separate strings: 
    one containing all the alphabetic characters and the other containing all the numeric characters.

    Args:
        s (str): The input alphanumeric string.

    Returns:
        tuple: A tuple of two strings, the first containing all the alphabetic characters and the second containing all the numeric characters.
    """
    alpha = ""
    numeric = ""
    for character in s:
        if character.isalpha():
            alpha += character
        elif character.isdigit():
            numeric += character
    return alpha, numeric