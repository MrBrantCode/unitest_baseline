"""
QUESTION:
Create a function `are_anagrams` that takes two strings as input and returns `True` if they are anagrams and `False` otherwise. The function should consider the strings case-insensitive, ignore any leading or trailing white spaces, and exclude special characters. The function should not take any other input.
"""

import string

def are_anagrams(str1, str2):
    """
    This function checks if two strings are anagrams.
    
    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.
    
    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    
    # Remove leading and trailing white spaces from the strings
    str1 = str1.strip()
    str2 = str2.strip()

    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Remove special characters from the strings
    str1 = str1.translate(str.maketrans('', '', string.punctuation))
    str2 = str2.translate(str.maketrans('', '', string.punctuation))

    # Sort both strings alphabetically and compare
    return ''.join(sorted(str1)) == ''.join(sorted(str2))