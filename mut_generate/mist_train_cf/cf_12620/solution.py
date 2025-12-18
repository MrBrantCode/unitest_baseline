"""
QUESTION:
Write a function named `count_uppercase_chars` that takes a string as input and returns the number of uppercase characters in the string, given that the string contains at least one lowercase character.
"""

def count_uppercase_chars(s):
    """
    This function takes a string as input and returns the number of uppercase characters in the string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of uppercase characters in the string.
    """
    count = 0
    for char in s:
        if char.isupper():
            count += 1
    return count