"""
QUESTION:
Create a function named `are_anagrams` that checks whether two input strings are anagrams of each other. The function should be case-insensitive and ignore non-alphanumeric characters. It must be efficient enough to handle large strings. The function should return `True` if the strings are anagrams and `False` otherwise.
"""

def are_anagrams(str1, str2):
    """
    Checks if two strings are anagrams of each other, ignoring non-alphanumeric characters and case.

    Args:
        str1 (str): The first string to compare.
        str2 (str): The second string to compare.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    
    # Convert both strings to lower case and remove non-alphanumeric characters
    str1 = ''.join(char.lower() for char in str1 if char.isalnum())
    str2 = ''.join(char.lower() for char in str2 if char.isalnum())

    # Check if lengths are not equal
    if len(str1) != len(str2):
        return False

    # Sort both strings and check if they are equal
    return sorted(str1) == sorted(str2)