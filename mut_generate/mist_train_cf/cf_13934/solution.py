"""
QUESTION:
Write a function called `check_strings` that takes two strings of different lengths as input and returns True if one string is equal to the other or if one string is a substring of the other, and False otherwise.
"""

def check_strings(string1, string2):
    """
    Checks if two strings are equal or if one string is a substring of the other.

    Args:
        string1 (str): The first string to compare.
        string2 (str): The second string to compare.

    Returns:
        bool: True if the strings are equal or if one string is a substring of the other, False otherwise.
    """
    # Compare the lengths of the strings
    if len(string1) == len(string2):
        # Compare the characters of the strings
        return string1 == string2
    else:
        # If the lengths are different, check if one string is a substring of the other
        return string1 in string2 or string2 in string1