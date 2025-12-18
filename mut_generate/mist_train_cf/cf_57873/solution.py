"""
QUESTION:
Create a function `are_anagrams` that takes two strings as arguments and returns `True` if they are anagrams (same letters arranged differently) and `False` otherwise. The function should ignore capitalization, punctuation, and whitespace. It should be efficient for large-sized strings.
"""

def are_anagrams(str_1, str_2):
    """
    This function checks if two given strings are anagrams.
    
    It first removes all non-alphabet characters and converts the strings to lower case.
    Then it sorts the characters in both strings alphabetically and compares them.
    
    Args:
        str_1 (str): The first string to compare.
        str_2 (str): The second string to compare.
    
    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    str_1 = ''.join(e for e in str_1 if e.isalnum()).lower()
    str_2 = ''.join(e for e in str_2 if e.isalnum()).lower()
    return sorted(str_1) == sorted(str_2)