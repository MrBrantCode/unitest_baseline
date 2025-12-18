"""
QUESTION:
Create a function called `isRotation` that takes two strings and their corresponding lengths as input. The function should return True if the second string is a rotation of the first string, and False otherwise. The lengths of the strings are given as separate parameters.
"""

def isRotation(string1, string2, length1, length2):
    """
    Checks if the second string is a rotation of the first string.

    Args:
    string1 (str): The original string.
    string2 (str): The string to be checked.
    length1 (int): The length of the original string.
    length2 (int): The length of the string to be checked.

    Returns:
    bool: True if string2 is a rotation of string1, False otherwise.
    """
    if length1 == length2 and len(string1) > 0:
        return string2 in string1 + string1